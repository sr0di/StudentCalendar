# Generated by Django 2.2 on 2019-05-07 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_an'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denr', models.CharField(max_length=5)),
                ('an', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.An')),
            ],
        ),
    ]
