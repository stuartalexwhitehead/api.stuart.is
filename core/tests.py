from django.test.testcases import TestCase
from rest_framework.test import APIClient
from rest_framework.status import HTTP_200_OK


class WagtailApiTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_pages_endpoint(self):
        response = self.client.get('/pages/', format='json')

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response['content-type'], 'application/json')

    def test_images_endpoint(self):
        response = self.client.get('/images/', format='json')

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response['content-type'], 'application/json')

    def test_documents_endpoint(self):
        response = self.client.get('/documents/', format='json')

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response['content-type'], 'application/json')
