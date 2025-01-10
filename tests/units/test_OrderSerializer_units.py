from django.test import TestCase
from base.models import Order, OrderItem, ShippingAddress, Product
from base.serializers import OrderSerializer
from django.contrib.auth.models import User

class OrderSerializerTest(TestCase):

    def setUp(self):
        """
        Set up test data:
        - Create a test user.
        - Create an order associated with the user.
        - Create a product for the order item.
        - Create order items and a shipping address linked to the order.
        - Initialize the OrderSerializer with the order instance.
        """
        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword"
        )
        
        # Create product
        self.product = Product.objects.create(
            user=self.user,
            name="Test Product",
            price=50.00,
            brand="Test Brand",
            countInStock=100
        )

        # Create order
        self.order = Order.objects.create(
            user=self.user,
            paymentMethod="PayPal",
            taxPrice=10.00,
            shippingPrice=5.00,
            totalPrice=115.00
        )

        # Create order item
        self.order_item = OrderItem.objects.create(
            product=self.product,
            order=self.order,
            name="Test Product",
            qty=2,
            price=50.00
        )

        # Create shipping address
        self.shipping_address = ShippingAddress.objects.create(
            order=self.order,
            address="123 Test St",
            city="Test City",
            postalCode="12345",
            country="Test Country",
            shippingPrice=5.00
        )

        # Initialize serializer
        self.serializer = OrderSerializer(instance=self.order)

    def test_order_serializer_fields(self):
        """
        Test that all expected fields are serialized.
        """
        data = self.serializer.data
        self.assertIn("orderItems", data)
        self.assertIn("shippingAddress", data)
        self.assertIn("User", data)
        self.assertIn("paymentMethod", data)
        self.assertIn("totalPrice", data)

    def test_order_items_serialization(self):
        """
        Test the serialization of order items.
        """
        data = self.serializer.data["orderItems"]
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Test Product")
        self.assertEqual(data[0]["qty"], 2)
        self.assertEqual(data[0]["price"], "50.00")

    def test_shipping_address_serialization(self):
        """
        Test the serialization of the shipping address.
        """
        data = self.serializer.data["shippingAddress"]
        self.assertEqual(data["address"], "123 Test St")
        self.assertEqual(data["city"], "Test City")
        self.assertEqual(data["postalCode"], "12345")
        self.assertEqual(data["country"], "Test Country")

    def test_user_serialization(self):
        """
        Test the serialization of the user.
        """
        data = self.serializer.data["User"]
        self.assertEqual(data["email"], "testuser@example.com")
