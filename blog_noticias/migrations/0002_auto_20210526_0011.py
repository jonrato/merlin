# Generated by Django 3.1.7 on 2021-05-26 03:11

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_noticias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='postpost',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=True, editable=False, populate_from='title'),
        ),
        migrations.AddField(
            model_name='postpost',
            name='tags',
            field=models.ManyToManyField(to='blog_noticias.Category'),
        ),
    ]
