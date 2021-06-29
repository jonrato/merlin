# Generated by Django 3.1.7 on 2021-06-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0020_dashboard_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='dashboard_videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_capa', models.ImageField(blank=True, null=True, upload_to='')),
                ('titulo_capa', models.TextField()),
                ('text_capa', models.TextField()),
                ('link_capa', models.TextField()),
            ],
        ),
    ]