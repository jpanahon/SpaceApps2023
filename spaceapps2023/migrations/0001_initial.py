# Generated by Django 4.2.6 on 2023-10-08 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=51)),
                ('population', models.CharField(max_length=66)),
                ('status', models.CharField(max_length=15)),
                ('last_assessment_date', models.DateTimeField()),
                ('scientific_name', models.CharField(max_length=41)),
                ('legal_common_name', models.CharField(max_length=41)),
                ('legal_population', models.CharField(max_length=66)),
                ('schedule_status', models.CharField(max_length=15)),
                ('sara_schedule', models.CharField(max_length=11)),
                ('listed_on', models.DateTimeField()),
                ('location', models.CharField(max_length=227)),
                ('taxonomic_group', models.CharField(max_length=21)),
                ('under_consideration_for', models.CharField(max_length=13)),
                ('gic_decision', models.CharField(max_length=36)),
            ],
        ),
    ]
