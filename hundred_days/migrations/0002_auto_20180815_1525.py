# Generated by Django 2.0.5 on 2018-08-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hundred_days', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hproject',
            name='Summary',
            field=models.CharField(max_length=450),
        ),
        migrations.AlterField(
            model_name='hproject',
            name='category1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hproject',
            name='category2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hproject',
            name='category3',
            field=models.CharField(max_length=50),
        ),
    ]