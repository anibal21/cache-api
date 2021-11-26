from unittest import TestCase
from config.app import create_app
import json

class ObjectResourceTestCase(TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client(use_cookies=True)

    def test_empty_get(self):
        res = self.client.get(
            "/v1/objects/1",
            headers={
                "Content-Type": "application/json",
            },
        )

        self.assertEqual(res.status_code, 404)

    def test_found_item_get(self):
        res = self.client.post(
            "/v1/objects/1?ttl=0",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "cuenta": 4,
                "name": "test4",
                "age": 14
            })
        )
        res2 = self.client.get(
            "/v1/objects/1",
            headers={
                "Content-Type": "application/json",
            },
        )
        self.assertEqual(res2.status_code, 200)

    def test_delete_item(self):
        self.client.post(
            "/v1/objects/1?ttl=0",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "cuenta": 4,
                "name": "test4",
                "age": 14
            })
        )
        res = self.client.delete(
            "/v1/objects/1",
            headers={
                "Content-Type": "application/json",
            },
        )
        self.assertEqual(res.status_code, 200)

    def test_put_item(self):
        self.client.post(
            "/v1/objects/1?ttl=0",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "cuenta": 4,
                "name": "test4",
                "age": 14
            })
        )
        res2 = self.client.put(
            "/v1/objects/1",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "cuenta": 1,
                "name": "test2",
                "age": 12,
                "parent": 15
            })
        )
        
        self.assertEqual(res2.status_code, 200)

    def test_reject_item(self):
        self.client.post(
            "/v1/objects/1?ttl=0",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "cuenta": 4,
                "name": "test4",
                "age": 14
            })
        )
        self.client.post(
            "/v1/objects/2?ttl=0",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "cuenta": 4,
                "name": "test4",
                "age": 14
            })
        )
        res= self.client.post(
            "/v1/objects/3?ttl=0",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "cuenta": 4,
                "name": "test4",
                "age": 14
            })
        )
        self.assertEqual(res.status_code, 507)