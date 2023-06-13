# Generated by Django 4.2.1 on 2023-06-08 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EMSAPI', '0011_alter_company_name_company_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_skill', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='employeedata',
            name='skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EMSAPI.employee_skill'),
        ),
    ]