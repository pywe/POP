# Generated by Django 2.1.4 on 2020-05-03 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0013_remove_child_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugreference',
            name='inn',
            field=models.ForeignKey(help_text='Active ingredient in the drug. eg. paracetamol', null=True, on_delete=django.db.models.deletion.SET_NULL, to='campaigns.Inn'),
        ),
    ]
