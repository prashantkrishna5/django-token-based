# Generated by Django 3.0.8 on 2020-07-12 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testquery',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
