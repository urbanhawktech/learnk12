from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models, connection
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from modelcluster.fields import ParentalKey


class CourseReview(models.Model):
    course_page = ParentalKey(
        'CoursePage',
        on_delete=models.CASCADE,
        related_name='course_reviews'
    )

    # meta settings
    parent_page_type = ['CoursePage']
    subpage_types = []

    # database fields
    score = models.PositiveSmallIntegerField(db_index=True, validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    publish_date = models.DateTimeField(db_index=True, auto_now_add=True)
    subject = models.TextField(db_index=True)
    description = models.TextField(db_index=True)
    date_modified = models.DateTimeField(db_index=True, auto_now=True)

    class ReviewerType(models.TextChoices):
        STUDENT = 'student'
        PARENT = 'parent'
        TEACHER = 'teacher'
    reviewer_type = models.CharField(choices=ReviewerType.choices, max_length=24)

    name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True)


@receiver(post_save, sender=CourseReview, dispatch_uid="post_save_course_agg_fields")
def post_save_course_agg_fields(sender, instance, **kwargs):
    post_save_course_page(instance)
    post_save_provider_page(instance)


@receiver(post_delete, sender=CourseReview, dispatch_uid="post_delete_course_agg_fields")
def post_delete_course_agg_fields(sender, instance, **kwargs):
    course_review = CourseReview.objects.filter(course_page_id=instance.course_page_id). \
        order_by('-date_modified').first()
    if course_review:
        post_save_course_agg_fields(sender, course_review, **kwargs)
    else:
        raw_sql_update = (
            'UPDATE home_coursepage '
            'SET avg_score = null, review_count = 0 '
            'WHERE page_ptr_id = {course_id} '
            'AND (SELECT page_ptr_id '
            'FROM home_coursereview '
            'WHERE course_page_id = {course_id} '
            'ORDER BY date_modified DESC LIMIT 1) IS NULL'
        )
        with connection.cursor() as cursor:
            cursor.execute(raw_sql_update.format(course_id=instance.course_page_id))

        raw_sql_update = (
            'UPDATE home_providerpage '
            'SET avg_score = null, review_count = 0 '
            'WHERE page_ptr_id = (SELECT provider_id'
            'FROM home_coursepage '
            'WHERE course.page_ptr_id = {course_id }) '
            'AND (SELECT page_ptr_id '
            'FROM home_coursereview '
            'WHERE course_page_id = {course_id} '
            'ORDER BY date_modified DESC LIMIT 1) IS NULL'
        )
        with connection.cursor() as cursor:
            cursor.execute(raw_sql_update.format(course_id=instance.course_page_id))


def post_save_course_page(instance):
    raw_sql_select = (
        'SELECT page_ptr_id, AVG(review.score), COUNT(*) '
        'FROM home_coursepage AS course '
        'JOIN home_coursereview AS review ON review.course_page_id = course.page_ptr_id '
        'WHERE course.page_ptr_id = {course_id} '
        'GROUP BY page_ptr_id'
    )
    # To minimize race conditions, this SQL update clause also checks that this CourseReview instance
    # matches the most recently modified home_coursereview for all of the related home_coursepage
    # There still exists a race condition between the UPDATE and the SELECT subquery
    raw_sql_update = (
        'UPDATE home_coursepage '
        'SET avg_score = {avg_score}, review_count = {review_count} '
        'WHERE page_ptr_id = {course_id} '
        'AND {review_id} = (SELECT id '
        'FROM home_coursereview '
        'WHERE course_page_id = {course_id} '
        'ORDER BY date_modified DESC LIMIT 1)'
    )
    with connection.cursor() as cursor:
        cursor.execute(raw_sql_select.format(course_id=instance.course_page_id))
        course_id, avg_score, review_count = cursor.fetchone()
        cursor.execute(raw_sql_update.format(
            avg_score=avg_score,
            review_count=review_count,
            course_id=course_id,
            review_id=instance.id
        ))


def post_save_provider_page(instance):
    raw_sql_select = (
        'SELECT provider.page_ptr_id, AVG(review.score), COUNT(*) '
        'FROM home_providerpage AS provider '
        'JOIN home_coursepage AS course ON course.provider_id = provider.page_ptr_id '
        'JOIN home_coursereview AS review ON review.course_page_id = course.page_ptr_id '
        'WHERE provider.page_ptr_id = (SELECT provider_id '
        'FROM home_coursepage '
        'WHERE page_ptr_id = {course_id}) '
        'GROUP BY provider.page_ptr_id'
    )
    raw_sql_update = (
        'UPDATE home_providerpage '
        'SET avg_score = {avg_score}, review_count = {review_count} '
        'WHERE page_ptr_id = {provider_id} '
        'AND {review_id} = (SELECT id '
        'FROM home_coursereview '
        'WHERE course_page_id = {course_id} '
        'ORDER BY date_modified DESC LIMIT 1)'
    )
    with connection.cursor() as cursor:
        cursor.execute(raw_sql_select.format(course_id=instance.course_page_id))
        provider_id, avg_score, review_count = cursor.fetchone()
        cursor.execute(raw_sql_update.format(
            avg_score=avg_score,
            review_count=review_count,
            provider_id=provider_id,
            review_id=instance.id,
            course_id=instance.course_page_id,
        ))
