# Generated by Django 2.2 on 2019-05-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0006_auto_20190521_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repart',
            name='tip_activitate',
            field=models.CharField(choices=[('C', 'Curs'), ('S', 'Seminar'), ('L', 'Laborator')], max_length=1),
        ),
    ]
