# Generated by Django 3.1.7 on 2021-05-31 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0005_auto_20210531_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_assinaturas',
            old_name='slug',
            new_name='slugf',
        ),
    ]