# Generated by Django 2.2 on 2019-05-21 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190521_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='limbapredare',
            name='specializare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='limbi_predare', to='accounts.Specializare'),
        ),
    ]
