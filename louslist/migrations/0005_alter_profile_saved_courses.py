# Generated by Django 4.1.1 on 2022-11-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('louslist', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='saved_courses',
            field=models.JSONField(default=list, null=True),
        ),
    ]
