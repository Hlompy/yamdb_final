# Generated by Django 2.2.16 on 2022-02-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'User role'), ('moderator', 'Moderator role'), ('admin', 'Administrator role')], default='user', max_length=15, verbose_name='Пользовательская роль'),
        ),
    ]
