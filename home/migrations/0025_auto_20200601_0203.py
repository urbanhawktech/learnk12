# Generated by Django 3.0.5 on 2020-06-01 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20200601_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetailpage',
            name='course_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
