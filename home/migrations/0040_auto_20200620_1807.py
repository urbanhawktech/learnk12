# Generated by Django 3.0.5 on 2020-06-20 18:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0039_coursespage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoursesPage',
            new_name='AllCoursesPage',
        ),
    ]
