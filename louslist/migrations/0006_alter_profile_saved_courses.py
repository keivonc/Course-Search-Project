# Generated by Django 4.1.1 on 2022-11-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('louslist', '0005_alter_profile_saved_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='saved_courses',
            field=models.JSONField(default=list),
        ),
    ]