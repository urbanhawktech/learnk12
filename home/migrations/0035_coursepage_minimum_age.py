# Generated by Django 3.0.5 on 2020-06-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20200619_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepage',
            name='minimum_age',
            field=models.PositiveSmallIntegerField(db_index=True, default=5),
            preserve_default=False,
        ),
    ]
