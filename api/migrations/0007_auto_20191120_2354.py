# Generated by Django 2.2.5 on 2019-11-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20191115_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='female',
            name='recommend_user',
            field=models.TextField(blank=True, default='|'),
        ),
        migrations.AddField(
            model_name='male',
            name='recommend_user',
            field=models.TextField(blank=True, default='|'),
        ),
    ]