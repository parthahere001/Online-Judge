# Generated by Django 3.0.6 on 2020-05-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0007_auto_20200511_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_memory_limit',
            field=models.IntegerField(default=50000, help_text='Memory Limit for the question'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_time_limit',
            field=models.IntegerField(default=1, help_text='Time Limit for the question'),
        ),
    ]
