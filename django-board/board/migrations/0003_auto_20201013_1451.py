# Generated by Django 3.1.2 on 2020-10-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20201013_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
