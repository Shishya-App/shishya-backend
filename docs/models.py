from django.db import models


class PDF(models.Model):
    name = models.CharField(max_length=20, blank=True)
    pdf = models.FileField(upload_to="docs", blank=True)

    def __str__(self):
        return self.name