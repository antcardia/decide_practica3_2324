from django.db import models


class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()
    adscripcion = models.CharField(max_length=256, default='none') 
    hola

    class Meta:
        unique_together = (('voting_id', 'voter_id'),)
