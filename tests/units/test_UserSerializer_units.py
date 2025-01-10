from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from base.serializers import UserSerializer

class UserSerializerTest(TestCase):

    def setUp(self):
        """
        Set up test data:
        - Creates a sample user with a username, email, and password.
        - Initializes a UserSerializer with the user instance.
        """
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword"
        )
        self.serializer = UserSerializer(instance=self.user)

    def test_user_serializer_fields(self):
        
        """
        Test that the serialized user data contains all required fields:
        - 'id', '_id', 'username', 'email', 'name', and 'isAdmin'.
        """
        data = self.serializer.data
        self.assertIn("id", data)
        self.assertIn("_id", data)
        self.assertIn("username", data)
        self.assertIn("email", data)
        self.assertIn("name", data)
        self.assertIn("isAdmin", data)

    def test_get_name(self):
        """
        Test the `get_name` method of the UserSerializer:
        - Ensures it returns the user's first name if set.
        - Defaults to the user's email if the first name is empty.
        """
        self.assertEqual(self.serializer.get_name(self.user), self.user.first_name or self.user.email)

    def test_get_is_admin(self):
        """
        Test the `get_isAdmin` method of the UserSerializer:
        - Ensures it correctly identifies if the user is an admin (staff).
        """
        self.assertEqual(self.serializer.get_isAdmin(self.user), self.user.is_staff)

    def test_serializer_output(self):
        """
        Test the serialized output of the user:
        - Verifies the email matches the test user's email.
        - Ensures 'name' defaults to email since first_name is empty.
        - Confirms 'isAdmin' is False for a non-admin user.
        """
        data = self.serializer.data
        self.assertEqual(data["email"], "testuser@example.com")
        self.assertEqual(data["name"], "testuser@example.com")  # Since first_name is empty
        self.assertEqual(data["isAdmin"], False)  # Default user is not an admin
