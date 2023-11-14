# Generated by Django 4.2.6 on 2023-11-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_remove_section_courseid_section_crn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='CRN',
            new_name='crn',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='deliveryType',
            new_name='delivery_type',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='meetingType',
            new_name='meeting_type',
        ),
        migrations.RemoveField(
            model_name='section',
            name='offeringTime',
        ),
        migrations.AddField(
            model_name='section',
            name='offering_time',
            field=models.CharField(default='', verbose_name=255),
            preserve_default=False,
        ),
    ]
