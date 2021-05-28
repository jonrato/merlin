# Generated by Django 3.1.7 on 2021-05-28 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0003_assinaturas_cursos'),
    ]

    operations = [
        migrations.CreateModel(
            name='aprender_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprender', models.TextField(default='Página Home')),
            ],
        ),
        migrations.CreateModel(
            name='assinaturas_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assinaturas', models.TextField(default='Página Home')),
            ],
        ),
        migrations.CreateModel(
            name='home_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.TextField(default='Página Home')),
            ],
        ),
        migrations.CreateModel(
            name='login_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField(default='Página Home')),
            ],
        ),
        migrations.CreateModel(
            name='noticias_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noticias', models.TextField(default='Página Home')),
            ],
        ),
        migrations.CreateModel(
            name='sobre_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sobre', models.TextField(default='Página Home')),
            ],
        ),
    ]
