# Generated by Django 2.2.8 on 2022-11-22 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20221023_0633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='count_of_commnet',
            new_name='count_of_comment',
        ),
    ]
