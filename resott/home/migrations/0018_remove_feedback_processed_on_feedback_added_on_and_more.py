# Generated by Django 4.0.1 on 2022-05-22 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='processed_on',
        ),
        migrations.AddField(
            model_name='feedback',
            name='added_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.restprofile'),
        ),
    ]
