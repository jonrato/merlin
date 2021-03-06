# Generated by Django 3.1.7 on 2021-09-19 21:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, verbose_name='Nome do Produto')),
                ('description', models.TextField(max_length=800, verbose_name='Descrição')),
                ('price', models.TextField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(20000)], verbose_name='Preço')),
            ],
        ),
    ]
