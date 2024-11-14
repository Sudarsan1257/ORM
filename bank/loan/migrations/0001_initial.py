# Generated by Django 5.1.3 on 2024-11-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loan_DB',
            fields=[
                ('Customer_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Customer_name', models.CharField(max_length=100)),
                ('loan_no', models.IntegerField()),
                ('loan_amount', models.IntegerField()),
                ('Mail_ID', models.EmailField(max_length=254)),
            ],
        ),
    ]