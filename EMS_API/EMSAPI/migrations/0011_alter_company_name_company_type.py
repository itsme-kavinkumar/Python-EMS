# Generated by Django 4.2.1 on 2023-06-06 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EMSAPI', '0010_type_of_company_alter_employeedata_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_name',
            name='company_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmpmytyp', to='EMSAPI.type_of_company'),
        ),
    ]
