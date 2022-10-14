# Generated by Django 4.1.2 on 2022-10-14 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_job_user_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to='tracker.job'),
        ),
    ]
