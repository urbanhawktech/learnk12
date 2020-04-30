# Generated by Django 3.0.5 on 2020-04-30 22:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200430_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('publish_date', models.DateField()),
                ('subject', models.TextField()),
                ('description', models.TextField()),
                ('reviewer_type', models.CharField(choices=[('student', 'Student'), ('parent', 'Parent'), ('teacher', 'Teacher'), ('business', 'Business')], max_length=24)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('is_anonymous', models.BooleanField()),
                ('course_detail_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_reviews', to='home.CourseDetailPage')),
            ],
        ),
    ]
