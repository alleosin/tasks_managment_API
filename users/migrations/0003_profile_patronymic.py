# Generated by Django 5.0.6 on 2024-06-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(default='otczestvo', max_length=150),
            preserve_default=False,
        ),
    ]