# Generated by Django 4.2.1 on 2023-06-10 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EMSAPI', '0013_skill_remove_employee_skill_employee_skill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='Role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emplemplrl', to='EMSAPI.employee_role'),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='Salarytype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emplempltyp', to='EMSAPI.salary_type'),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='employee_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emplemplemptp', to='EMSAPI.employees_type'),
        ),
    ]