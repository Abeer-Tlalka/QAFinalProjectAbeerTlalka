from django.test import TestCase
from base.models import Product, Review
from base.serializers import ProductSerializer
from django.contrib.auth.models import User

class ProductSerializerTest(TestCase):

    def setUp(self):
        """
        Set up test data:
        - Creates a test user, a product, and two reviews for the product.
        - Initializes a ProductSerializer with the product instance.
        """
        self.user = User.objects.create_user(username="testuser", email="testuser@example.com", password="testpassword")
        self.product = Product.objects.create(name="Test Product", price=100)
        self.review1 = Review.objects.create(user=self.user, product=self.product, rating=5, comment="Great product!")
        self.review2 = Review.objects.create(user=self.user, product=self.product, rating=4, comment="Good product!")
        self.serializer = ProductSerializer(instance=self.product)

    def test_product_serializer_fields(self):
        """
        Test that the serialized product data contains the required fields:
        - 'name', 'price', and 'reviews'.
        """
        data = self.serializer.data
        self.assertIn("reviews", data)
        self.assertIn("name", data)
        self.assertIn("price", data)

    def test_product_reviews(self):
        """
        Test that the serialized product includes all associated reviews with correct details:
        - Ensures the number of reviews is correct.
        - Checks the ratings of each review.
        """
        data = self.serializer.data
        self.assertEqual(len(data["reviews"]), 2)  # Should return both reviews
        self.assertEqual(data["reviews"][0]["rating"], 5)
        self.assertEqual(data["reviews"][1]["rating"], 4)
