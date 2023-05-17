# Generated by Django 4.1.4 on 2023-02-05 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0007_alter_issuerequestmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedBooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.bookmodel')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.membermodel')),
            ],
        ),
    ]