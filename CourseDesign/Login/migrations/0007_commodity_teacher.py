# Generated by Django 3.1.1 on 2020-09-19 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_auto_20200917_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('ID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('Description', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Login.account')),
                ('name', models.CharField(max_length=20)),
                ('isMale', models.BooleanField(default=True)),
            ],
        ),
    ]
