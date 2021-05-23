from django.db import models
from django.urls import reverse

class AttendanceTablet(models.Model):
    name = models.CharField(max_length=120, null=False)
    online = models.BooleanField(default=False, null=False)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("attendance_tablet-show", kwargs={"id": self.id})
