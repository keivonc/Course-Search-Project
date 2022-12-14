# Generated by Django 4.1.1 on 2022-11-11 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('louslist', '0015_profile_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='saved_courses',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('commenter', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_commenter_set', to='louslist.profile')),
                ('profile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='commend_profile_set', to='louslist.profile')),
            ],
        ),
    ]
