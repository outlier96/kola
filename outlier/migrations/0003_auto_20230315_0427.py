# Generated by Django 3.2.15 on 2023-03-14 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outlier', '0002_post_slugs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='slugs',
            new_name='slug',
        ),
    ]
