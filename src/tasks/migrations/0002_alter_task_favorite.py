# Generated by Django 4.0.6 on 2022-07-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='favorite',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
