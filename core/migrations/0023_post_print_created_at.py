# Generated by Django 2.2.8 on 2023-01-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20230124_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='print_created_at',
            field=models.CharField(default='', max_length=10),
        ),
    ]
