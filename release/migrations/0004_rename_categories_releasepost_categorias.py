# Generated by Django 3.2.7 on 2021-11-18 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0003_alter_releasepost_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='releasepost',
            old_name='categories',
            new_name='categorias',
        ),
    ]