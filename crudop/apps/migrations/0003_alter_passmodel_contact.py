# Generated by Django 4.1.5 on 2023-02-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_passmodel_aadhar_alter_passmodel_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passmodel',
            name='contact',
            field=models.IntegerField(max_length=10),
        ),
    ]
