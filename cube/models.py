from django.db import models


class Cube(models.Model):

    identifier = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.identifier
