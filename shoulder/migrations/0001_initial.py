# Generated by Django 4.0.1 on 2022-01-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoulder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.IntegerField()),
            ],
            options={
                'db_table': 'shoulder_cnt',
                'managed': False,
            },
        ),
    ]
