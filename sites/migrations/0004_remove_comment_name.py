# Generated by Django 4.1.1 on 2022-09-30 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_remove_comment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]