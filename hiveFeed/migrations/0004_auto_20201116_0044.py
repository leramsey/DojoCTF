# Generated by Django 3.1.3 on 2020-11-16 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hiveFeed', '0003_auto_20201115_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='hivepost',
            name='post_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hivepost',
            name='post_body',
            field=models.TextField(default='body'),
        ),
        migrations.AlterField(
            model_name='hivepost',
            name='post_title',
            field=models.CharField(default='title', max_length=50),
        ),
    ]