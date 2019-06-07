# Generated by Django 2.2 on 2019-05-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190521_1643'),
        ('cal', '0011_auto_20190523_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='structurasemestru',
            name='limbi_predare',
            field=models.ManyToManyField(to='accounts.LimbaPredare'),
        ),
        migrations.AlterField(
            model_name='repart',
            name='tip_activitate',
            field=models.CharField(choices=[('S', 'Seminar'), ('C', 'Curs'), ('L', 'Laborator')], max_length=1),
        ),
    ]
