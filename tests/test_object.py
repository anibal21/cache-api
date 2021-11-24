from unittest import TestCase
from api.app import create_app

class ObjectResourceTestCase(TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client(use_cookies=True)

    def test_get(self):
        res = self.client.get(
            "/v1/object/",
            headers={
                "Content-Type": "application/json",
            },
        )

        self.assertEqual(res.status_code, 200)