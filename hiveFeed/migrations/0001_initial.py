# Generated by Django 3.1.3 on 2020-11-15 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hivePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(default='Empty Title', max_length=50)),
                ('post_body', models.CharField(default='Body of post here', max_length=100)),
            ],
        ),
    ]
