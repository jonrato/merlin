# Generated by Django 3.1.7 on 2021-05-26 19:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_noticias', '0007_auto_20210526_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
