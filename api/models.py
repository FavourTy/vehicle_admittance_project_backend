from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=1000)
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.CharField(max_length=11)
    plate_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
