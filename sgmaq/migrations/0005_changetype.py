# Generated by Django 4.2.2 on 2024-06-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgmaq', '0004_carmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changetype', models.CharField(max_length=100)),
            ],
        ),
    ]
