# Generated by Django 3.0.5 on 2020-05-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200522_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursespage',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coursespage',
            name='heading',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]