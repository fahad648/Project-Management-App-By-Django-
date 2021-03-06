# Generated by Django 3.2.11 on 2022-02-10 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManagement', '0002_remove_employees_employee_name2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(max_length=50)),
                ('Employee_id', models.CharField(max_length=50)),
                ('Employee_contact', models.CharField(max_length=50)),
                ('emp_status', models.CharField(max_length=50)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectManagement.projects')),
            ],
        ),
    ]
