# Generated by Django 5.0.6 on 2024-06-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_finished_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('WAITING', 'Waiting for executor'), ('IN_PROCESS', 'In process'), ('FINISHED', 'Finished')], default='Waiting for executor', max_length=20),
        ),
    ]
