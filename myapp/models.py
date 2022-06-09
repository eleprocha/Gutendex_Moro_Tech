from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Review(models.Model):
    bookId = models.IntegerField()
    rating = models.BigIntegerField(validators = [MinValueValidator(0),MaxValueValidator(5)])
    review = models.CharField(max_length=100)

#    return {self.bookId}
