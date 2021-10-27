# Generated by Django 3.2.7 on 2021-10-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('resume', models.CharField(max_length=50)),
                ('pdf', models.FileField(upload_to='pdf/')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
