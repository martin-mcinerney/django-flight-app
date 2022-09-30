# Generated by Django 4.1.1 on 2022-09-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_comment_email_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flyingsite',
            name='wind_direction',
            field=models.CharField(choices=[('N', 'N'), ('NE', 'NE'), ('E', 'E'), ('S', 'E'), ('S', 'S'), ('SW', 'SW'), ('W', 'W'), ('NW', 'NW')], max_length=150),
        ),
    ]
