# Generated by Django 4.2.2 on 2024-06-11 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgmaq', '0003_carbrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('brandname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgmaq.carbrand')),
            ],
        ),
    ]