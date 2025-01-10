from base.models import Product, Review
from base.serializers import ReviewSerializer
from django.test import TestCase
from django.contrib.auth.models import User
class ReviewSerializerTest(TestCase):

    def setUp(self):
        """
        Set up test data:
        - Creates a test user, a product, and a review for the product.
        - Initializes a ReviewSerializer with the review instance.
        """
        self.user = User.objects.create_user(username="testuser", email="testuser@example.com", password="testpassword")
        self.product = Product.objects.create(name="Test Product", price=100)
        self.review = Review.objects.create(user=self.user, product=self.product, rating=5, comment="Great product!")
        self.serializer = ReviewSerializer(instance=self.review)

    def test_review_serializer_fields(self):
        """
        Test that the serialized review data contains the required fields:
        - '_id', 'user', 'product', 'rating', and 'comment'.
        """
        data = self.serializer.data
        self.assertIn("_id", data)
        self.assertIn("user", data)
        self.assertIn("product", data)
        self.assertIn("rating", data)
        self.assertIn("comment", data)

    def test_review_serialization(self):
        """
        Test that the serialized review data is correct:
        - Ensures the 'rating' and 'comment' fields match the review instance.
        """
        # Ensure the correct review data is serialized
        data = self.serializer.data
        self.assertEqual(data["rating"], 5)
        self.assertEqual(data["comment"], "Great product!")
