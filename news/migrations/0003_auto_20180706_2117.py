# Generated by Django 2.0.2 on 2018-07-06 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]