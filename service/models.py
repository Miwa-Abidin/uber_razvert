from django.db import models
from accounts . models import Profile


class Taxi(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price} - {self.profile}'

class Order(models.Model):
    adress = models.CharField(max_length=20)
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.taxi.name


class StatusType(models.Model):
    slug = models.SlugField()
    rating = models.IntegerField()

    def __str__(self):
        return self.slug


class StatusDriver(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=1)
    point = models.IntegerField()
    type = models.ForeignKey(StatusType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.point} - {self.profile} - {self.type}'
