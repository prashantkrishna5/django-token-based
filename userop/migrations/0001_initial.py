# Generated by Django 3.0.8 on 2020-07-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=200)),
                ('ProblemID', models.IntegerField(default=0)),
                ('ProblemTitle', models.CharField(max_length=200)),
                ('MobileNubers', models.CharField(max_length=200)),
            ],
        ),
    ]