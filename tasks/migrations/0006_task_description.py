# Generated by Django 5.0.6 on 2024-06-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]