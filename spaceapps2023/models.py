from django.db import models

class Animals(models.Model):
    common_name = models.CharField(max_length=51, null=True)
    population = models.CharField(max_length=66, null=True)
    status = models.CharField(max_length=15, null=True)
    last_assessment_date = models.DateTimeField(null=True)
    scientific_name = models.CharField(max_length=41, null=True)
    legal_common_name = models.CharField(max_length=41, null=True)
    legal_population = models.CharField(max_length=66, null=True)
    schedule_status = models.CharField(max_length=15, null=True)
    sara_schedule = models.CharField(max_length=11, null=True)
    listed_on = models.DateTimeField(null=True)
    location = models.CharField(max_length=227, null=True)
    taxonomic_group = models.CharField(max_length=21, null=True)
    under_consideration_for = models.CharField(max_length=13, null=True)
    gic_decision = models.CharField(max_length=36, null=True)