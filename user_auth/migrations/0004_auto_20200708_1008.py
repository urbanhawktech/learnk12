# Generated by Django 3.0.5 on 2020-07-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20200708_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
