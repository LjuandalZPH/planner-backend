from django.test import TestCase


class GamificationRootTests(TestCase):
    def test_gamification_endpoint(self):
        resp = self.client.get("/api/gamification/")
        self.assertEqual(resp.status_code, 200)

