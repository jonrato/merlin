# Generated by Django 3.2.7 on 2021-10-26 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0002_alter_releasepost_overview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='releasepost',
            options={'ordering': ('-date',)},
        ),
    ]