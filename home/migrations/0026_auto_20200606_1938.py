# Generated by Django 3.0.5 on 2020-06-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20200601_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetailpage',
            name='difficulty',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Beginner'), (1, 'Basic'), (2, 'Intermediate'), (3, 'Proficient'), (4, 'Advanced')], db_index=True),
        ),
    ]
