# Generated by Django 3.1 on 2020-12-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_App', '0006_auto_20201207_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
