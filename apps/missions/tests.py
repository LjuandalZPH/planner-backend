from django.test import TestCase


class MissionsSmokeTests(TestCase):
    def test_missions_health(self):
        resp = self.client.get("/api/missions/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("message", resp.json())

