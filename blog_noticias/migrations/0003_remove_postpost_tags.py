# Generated by Django 3.1.7 on 2021-05-26 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_noticias', '0002_auto_20210526_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postpost',
            name='tags',
        ),
    ]
