# Generated by Django 2.0.5 on 2018-08-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_samples', '0009_auto_20180803_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksamples',
            name='challenges',
            field=models.CharField(max_length=200),
        ),
    ]
