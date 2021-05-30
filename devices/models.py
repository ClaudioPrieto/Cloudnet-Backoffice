from django.db import models
from django.urls import reverse

class Device(models.Model):
    name = models.CharField(max_length=120, null=False)
    description = models.TextField()
    price = models.IntegerField()
    point_of_sale = models.ForeignKey('point_of_sales.PointOfSale', on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("device-show", kwargs={"id": self.id})