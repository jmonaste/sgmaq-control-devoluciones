# Generated by Django 4.2.2 on 2024-06-11 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgmaq', '0010_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('task', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sgmaq.task')),
            ],
        ),
    ]
