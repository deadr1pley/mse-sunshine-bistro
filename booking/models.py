from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending"
    )

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
