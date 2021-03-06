# Generated by Django 3.1.7 on 2021-05-28 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admindashboard', '0007_home_view_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alguem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_nosso_time', models.TextField()),
                ('thumbnailA', models.ImageField(blank=True, null=True, upload_to='')),
                ('thumbnailB', models.ImageField(blank=True, null=True, upload_to='')),
                ('thumbnailC', models.ImageField(blank=True, null=True, upload_to='')),
                ('nameA', models.TextField()),
                ('nameB', models.TextField()),
                ('nameC', models.TextField()),
                ('paragraphy1', models.TextField()),
                ('paragraphyImage1', models.ImageField(blank=True, null=True, upload_to='')),
                ('paragraphy2', models.TextField()),
                ('paragraphyImage2', models.ImageField(blank=True, null=True, upload_to='')),
                ('comentario', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='home_view',
            name='auth',
        ),
        migrations.DeleteModel(
            name='Auth',
        ),
        migrations.DeleteModel(
            name='home_view',
        ),
    ]
