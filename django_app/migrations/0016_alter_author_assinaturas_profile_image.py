# Generated by Django 3.2.7 on 2021-10-21 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0015_alter_author_assinaturas_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author_assinaturas',
            name='profile_image',
            field=models.ImageField(upload_to='profile'),
        ),
    ]
