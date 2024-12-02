# Generated by Django 2.2.5 on 2021-07-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_auto_20210714_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='made_on',
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('10:00 A.M', '10:00 A.M'), ('10:30 A.M', '10:30 A.M'), ('11:00 A.M', '11:00 A.M'), ('11:30 A.M', '11:30 A.M'), ('12:00 P.M', '12:00 P.M'), ('12:30 P.M', '12:30 P.M'), ('01:00 P.M', '01:00 P.M'), ('01:30 P.M', '01:30 P.M'), ('05:00 P.M', '05:00 P.M'), ('05:30 P.M', '05:30 P.M'), ('06:00 P.M', '06:00 P.M'), ('06:30 P.M', '06:30 P.M'), ('07:00 P.M', '07:00 P.M'), ('07:30 P.M', '07:30 P.M'), ('08:00 P.M', '08:00 P.M'), ('08:30 P.M', '08:30 P.M')], default='', max_length=10),
        ),
    ]