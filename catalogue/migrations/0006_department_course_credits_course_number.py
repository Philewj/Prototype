# Generated by Django 4.2.6 on 2023-11-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_feedback_professorid_alter_feedback_sectionid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='number',
            field=models.CharField(default='', max_length=10, verbose_name='Course Number'),
            preserve_default=False,
        ),
    ]
