from django.db import models
from django.urls import reverse

class Device(models.Model):
    name = models.CharField(max_length=120, null=False)
    description = models.TextField()
    price = models.IntegerField()
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("device-show", kwargs={"id": self.id})