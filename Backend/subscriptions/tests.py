from django.test import TestCase, Client
import json

class CheckoutSessionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/api/create-checkout-session/"
        self.data = {
            "name": "Test User",
            "email": "test@example.com"
        }

    def test_checkout_session_returns_url(self):
        response = self.client.post(
            self.url,
            data=json.dumps(self.data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("url", response.json())
