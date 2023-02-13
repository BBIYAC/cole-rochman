# Generated by Django 2.2.8 on 2022-10-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20221007_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='vision',
            field=models.CharField(blank=True, default='', max_length=4, null=True, verbose_name='시력'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.CharField(blank=True, default='', max_length=7, null=True, verbose_name='몸무게'),
        ),
    ]
