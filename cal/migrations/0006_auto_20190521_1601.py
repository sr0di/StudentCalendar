# Generated by Django 2.2 on 2019-05-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0005_auto_20190511_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repart',
            name='tip_activitate',
            field=models.CharField(choices=[('L', 'Laborator'), ('C', 'Curs'), ('S', 'Seminar')], max_length=1),
        ),
    ]
