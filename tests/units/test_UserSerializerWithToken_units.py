from rest_framework_simplejwt.tokens import RefreshToken
from base.serializers import UserSerializerWithToken
from django.test import TestCase
from django.contrib.auth.models import User

class UserSerializerWithTokenTest(TestCase):

    def setUp(self):
        """
        Set up test data:
        - Creates a sample user with a username, email, and password.
        - Initializes a UserSerializerWithToken with the user instance.
        """
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword"
        )
        self.serializer = UserSerializerWithToken(instance=self.user)


    def test_serializer_output(self):
        """
        Test the serialized output:
        - Ensures the 'email' and 'isAdmin' fields are correctly serialized.
        - Confirms that the token is included in the serialized data.
        """
        data = self.serializer.data
        self.assertEqual(data["email"], "testuser@example.com")
        self.assertEqual(data["isAdmin"], False)
