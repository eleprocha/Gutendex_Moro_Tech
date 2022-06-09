from django.test import TestCase
from myapp.models import Review
# Create your tests here.



class ReviewTestCase(TestCase):
    def setUp(self):
        Review.objects.create(bookId=84, rating=4, review="Very Cool")
        Review.objects.create(bookId=68170, rating=6, review="Very Cool")

    def test_bookId(self):
        
        review = Review.objects.get(id = 1)
        field_label = review._meta.get_field('bookId').verbose_name
        self.assertEqual(field_label, 'bookId')
