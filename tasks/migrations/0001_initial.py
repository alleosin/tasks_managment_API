# Generated by Django 5.0.6 on 2024-06-25 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_rename_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WAITING', 'Waiting for executor'), ('IN_PROCESS', 'In process'), ('FINISHED', 'FINISHED')], default='Waiting for executor', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('finished_date', models.DateTimeField()),
                ('report', models.TextField()),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taken_tasks', to='users.profile')),
                ('orderer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to='users.profile')),
            ],
        ),
    ]
