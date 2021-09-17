from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from .models import Restaurant


class RestaurantAPITest(APITestCase):
    """Tests for the restaurant api"""

    RESTAURANTS_TO_CREATE = 10
    TEST_NAME = 'test_name'

    def setUp(self):
        restaurants = []
        for i in range(self.RESTAURANTS_TO_CREATE):
            restaurants.append(Restaurant(name=f'restaurant{i}'))

        Restaurant.objects.bulk_create(restaurants)

    def test_list_restaurants(self):
        """GET /restaurants/ returns 200 and the data list with length
        equal to the constant"""

        url = reverse('restaurants')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.RESTAURANTS_TO_CREATE)

    def test_create_restaurant(self):
        """POST /restaurants/ returns 201 and creates a Restaurants object only
        if the data is correct, otherwise returns 400 or 405, if the method
        is not allowed"""

        url = reverse('restaurants')
        # no data
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # method is not allowed
        response = self.client.put(url, {}, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.delete(url, {}, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        # wrong data
        response = self.client.post(url, {'wrong_data': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # trying to add with existing name
        response = self.client.post(
            url, {'name': Restaurant.objects.first().name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # no objects has been added
        self.assertEqual(Restaurant.objects.count(), self.RESTAURANTS_TO_CREATE)
        # correct data
        response = self.client.post(url, {'name': 'test_name'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # object has been created
        self.assertTrue(Restaurant.objects.filter(name='test_name').exists())

    def test_get_restaurant(self):
        """GET /restaurants/ returns 200 and an Restaurants object only
        if the name is correct, otherwise returns 400 or 405, if the method
        is not allowed"""
        url = reverse(f'restaurants_details', kwargs={'name': 'get_test'})
        # method is not allowed
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        # restaurant with such name does not exist
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_404_NOT_FOUND)
        Restaurant.objects.create(name='get_test')
        # correct name
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_restaurant(self):
        """PUT /restaurants/<str:name>/ returns 200 and updates the Restaurants
         object only if the data is correct, otherwise returns 400, 404"""

        url = reverse(f'restaurants_details', kwargs={'name': 'to_change'})
        # Restaurant with such name does not exist
        response = self.client.put(url, {}, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_404_NOT_FOUND)
        Restaurant.objects.create(name='to_change')
        # no data
        response = self.client.put(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # wrong data
        response = self.client.put(url, {'wrong_data': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # trying to change the name to an existing one
        response = self.client.put(
            url, {'name': Restaurant.objects.first().name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # correct data
        response = self.client.put(
            url, {'name': 'changed'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_restaurant(self):
        """DELETE /restaurants/<str:name>/ returns 204 and delete the
        Restaurants object only if the name is correct,
        otherwise returns 404"""

        url = reverse(f'restaurants_details', kwargs={'name': 'to_delete'})
        # Restaurant with such name does not exist
        response = self.client.put(url, {}, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_404_NOT_FOUND)
        Restaurant.objects.create(name='to_delete')
        # deletion
        response = self.client.delete(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_random_restaurant(self):
        """GET /restaurants_random/ returns 200 and a random
        Restaurant object"""

        url = reverse('restaurants_random')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)




