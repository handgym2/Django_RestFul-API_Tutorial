# Generated by Django 2.1 on 2019-03-10 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usnclass',
            name='student',
        ),
    ]