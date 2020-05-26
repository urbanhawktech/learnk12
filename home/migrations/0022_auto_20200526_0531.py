# Generated by Django 3.0.5 on 2020-05-26 05:31

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20200526_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='course_rank_tables',
            field=wagtail.core.fields.StreamField([('course_rank_table', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('filters', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.CharBlock()), ('value', wagtail.core.blocks.CharBlock())]))), ('excludes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.CharBlock()), ('value', wagtail.core.blocks.CharBlock())]))), ('sorts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('result_count', wagtail.core.blocks.IntegerBlock())]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]