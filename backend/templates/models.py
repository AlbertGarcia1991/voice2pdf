from django.db import models

# Create your models here.


class Template(models.Model):
    upload_id = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Template {self.upload_id}"


class Field(models.Model):
    template = models.ForeignKey("Template", related_name="fields", on_delete=models.CASCADE)
    field_id = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    label = models.CharField(max_length=128)
    placeholder = models.CharField(max_length=256, blank=True)
    page_number = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    validation = models.JSONField(default=dict)
    value = models.TextField(blank=True)

    def __str__(self):
        return f"{self.label} ({self.type})"
