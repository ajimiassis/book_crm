# Generated by Django 4.2.6 on 2023-11-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0007_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='course',
            field=models.CharField(max_length=20),
        ),
    ]
