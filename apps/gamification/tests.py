from django.test import TestCase


class GamificationSmokeTests(TestCase):
    def test_gamification_health(self):
        resp = self.client.get("/api/gamification/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("message", resp.json())

