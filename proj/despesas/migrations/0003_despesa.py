# Generated by Django 2.1.4 on 2018-12-18 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('despesas', '0002_delete_despesa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codfavorecido', models.CharField(max_length=50)),
                ('data', models.CharField(max_length=20)),
                ('fase', models.CharField(max_length=10)),
                ('favorecido', models.CharField(max_length=50)),
                ('valor', models.CharField(max_length=50)),
            ],
        ),
    ]
