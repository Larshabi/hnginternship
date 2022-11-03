from django.db import models

class Operations(models.Model):
    Operation_type_choices = (
        ('addition', 'addition',),
        ('subtraction', 'subtraction',),
        ('multiplication', 'multiplication')
        )
    operation_type = models.CharField(max_length=255, choices=Operation_type_choices)
    result = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    slackUsername = models.CharField(max_length=20, default='Lash')