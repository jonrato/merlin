# Generated by Django 3.1.7 on 2021-05-28 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0002_auto_20210525_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinaturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.CharField(blank=True, default=None, max_length=500, null=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.CharField(blank=True, default=None, max_length=500, null=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
