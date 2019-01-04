# Generated by Django 2.2 on 2019-01-03 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suspension_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Make', models.CharField(max_length=10)),
                ('Model', models.CharField(max_length=10)),
                ('Year', models.IntegerField()),
                ('Fork', models.CharField(max_length=20)),
                ('Shock', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='setting',
            name='Bike',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='suspension_settings.Bike'),
            preserve_default=False,
        ),
    ]
