from django.db import models

# Create your models here.
from django.db.models import CASCADE


from django.db import models

class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.username  # Useful for display in admin and related fields


class escalation_attack_detection(models.Model):
    user = models.ForeignKey(ClientRegister_Model, on_delete=models.CASCADE, default=1)  # Link to user
    subject = models.CharField(max_length=3000)
    email_message = models.CharField(max_length=3000)
    Prediction = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user.username} - {self.subject[:50]}"


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



