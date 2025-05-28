from django.db import models  # type: ignore
from django.utils import timezone  # type: ignore


class Voice2Pdf(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
