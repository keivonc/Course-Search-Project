# Generated by Django 3.2.16 on 2022-11-22 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('louslist', '0020_alter_comment_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_louslist_profile_friends_+', to='louslist.Profile'),
        ),
    ]
