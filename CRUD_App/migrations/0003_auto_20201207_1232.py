# Generated by Django 3.1 on 2020-12-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_App', '0002_auto_20201206_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
