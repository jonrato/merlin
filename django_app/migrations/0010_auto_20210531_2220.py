# Generated by Django 3.1.7 on 2021-06-01 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0009_auto_20210531_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_assinaturas',
            old_name='thumbnail',
            new_name='thumbnails',
        ),
    ]