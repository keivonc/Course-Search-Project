# Generated by Django 4.1.1 on 2022-11-07 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('louslist', '0008_alter_profile_saved_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='saved_sections',
            field=models.ManyToManyField(to='louslist.section'),
        ),
    ]
