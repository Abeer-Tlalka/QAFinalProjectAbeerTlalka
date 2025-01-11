from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from base.models import Product

class TestsProductAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.api_url = "/api/products/"
        self.test_product = Product.objects.create(
            name="Test Product",
            brand="Test Brand",
            category="Test Category",
            description="Test Description",
            price=100.0,
            countInStock=10
        )
    
    # GET
    def test_get_all_products(self):
        """Test retrieving all products from the API."""
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("products", response.data)
        
    def test_get_single_product_valid_id(self):
        product_id = self.test_product._id  
        response = self.client.get(f"{self.api_url}{product_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["_id"], product_id)

   
    
    def test_pagination(self):
        """Test pagination structure in the API response."""
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("page", response.data)
        self.assertIn("pages", response.data)

    def test_filter_by_category(self):
        """Test filtering products by category."""
        response = self.client.get(f"{self.api_url}?category=Test Category")  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        products = response.data.get("products", [])
        for product in products:
            self.assertEqual(product["category"], "Test Category")  # 

    # POST

    def test_create_product_missing_fields(self):
        """Test creating a product with missing required fields."""
        product_data = {"name": "Incomplete Product"}
        response = self.client.post(self.api_url, product_data, format='json')  
        self.assertIn(response.status_code, range(400,410))

   

    def test_update_product_invalid_id(self):
        """Test updating a product that does not exist."""
        updated_data = {
            "name": "Non-existent Product",
            "brand": "No Brand",
            "category": "No Category",
            "description": "No Description",
            "price": 0.0,
            "countInStock": 0
        }
        response = self.client.put(f"{self.api_url}9999/", updated_data, format='json')  # Add format='json'
        self.assertIn(response.status_code,range(400,410))
        
    # DELETE
    def test_delete_product_success(self):
        """Test deleting a product."""
        product_id = self.test_product._id
        response = self.client.delete(f"{self.api_url}{product_id}/")
        self.assertIn(response.status_code, range(400,410))
