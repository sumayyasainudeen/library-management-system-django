# Generated by Django 4.1.4 on 2023-02-06 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0015_delete_penaltymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenaltyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('return_date', models.DateField(auto_now_add=True)),
                ('over_due', models.IntegerField()),
                ('penalty', models.IntegerField()),
                ('reason', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.bookmodel')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.membermodel')),
            ],
        ),
    ]
