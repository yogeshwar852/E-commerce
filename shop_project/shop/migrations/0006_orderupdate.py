# Generated by Django 3.0.6 on 2020-05-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=1000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
