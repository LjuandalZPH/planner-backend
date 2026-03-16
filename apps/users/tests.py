from django.test import TestCase


class UsersSmokeTests(TestCase):
    def test_users_health(self):
        resp = self.client.get("/api/users/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("message", resp.json())

