# Generated by Django 4.1.5 on 2023-02-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passmodel',
            name='aadhar',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passmodel',
            name='contact',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='passmodel',
            name='pin',
            field=models.IntegerField(max_length=6),
        ),
    ]
