# Generated by Django 3.1.7 on 2021-05-28 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admindashboard', '0005_auto_20210528_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='home_view',
            name='auth',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to='admindashboard.auth'),
        ),
    ]
