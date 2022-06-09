from django import forms
from .models import Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = Review 
        # fields = ['bookId','rating','review']
        fields = "__all__"

        labels = {
            'bookId':'bookId',
            'rating':"rating",
            'review':'review'
        }
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes
        error_messages = {
            'rating':{
                'min_value':"Minimum value must be 0",
                'max_value':"Max value is 5"
            }
        }