# Generated by Django 3.1.7 on 2021-05-27 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_noticias', '0009_auto_20210527_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
