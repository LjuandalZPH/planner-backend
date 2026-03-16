from django.test import TestCase


class MissionsRootTests(TestCase):
    def test_missions_endpoint(self):
        resp = self.client.get("/api/missions/")
        self.assertEqual(resp.status_code, 200)

