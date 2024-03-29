# Generated by Django 2.1.4 on 2020-04-20 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0008_auto_20200110_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='campaign',
            field=models.ForeignKey(help_text='To what campaign is this session tied?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='campaigns.Campaign'),
        ),
    ]
