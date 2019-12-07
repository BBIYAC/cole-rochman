# Generated by Django 2.2.6 on 2019-12-07 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_notificationrecord_noti_time_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationrecord',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('SENDING', 'SENDING'), ('RETRY', 'RETRY'), ('RESERVED', 'RESERVED'), ('DELIVERED', 'DELIVERED'), ('SUSPENDED', 'SUSPENDED'), ('FAILED', 'FAILED'), ('CANCELED', 'CANCELED')], default='PENDING', max_length=20),
        ),
    ]
