from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Advantage


class AdvantageModelTest(TestCase):
    def setUp(self):
        Advantage.objects.create(title="Преимущество 1", content="Описание преимущества")

    def test_advantage_content(self):
        advantage = Advantage.objects.get(id=1)
        expected_object_title = f'{advantage.title}'
        expected_object_content = f'{advantage.content}'
        self.assertEqual(expected_object_title, "Преимущество 1")
        self.assertEqual(expected_object_content, "Описание преимущества")


class AdvantageModelTest2(APITestCase):

    def setUp(self):
        Advantage.objects.create(title="Тестовое преимущество", content="Описание тестового преимущества")

    def test_get_advantages(self):
        url = reverse('advantage-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Тестовое преимущество')
        self.assertEqual(response.data[0]['content'], 'Описание тестового преимущества')


class AdvantageAPITest(APITestCase):
    def test_get_advantages(self):
        url = reverse('advantage-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_MenuItems(self):
        url = reverse('menuitem-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AdvantageAPITestCase(APITestCase):

    def test_create_advantage(self):
        url = reverse('advantage-list')
        data = {'title': 'Новое преимущество',
                'content': 'Описание нового преимущества'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Advantage.objects.count(), 1)
        self.assertEqual(Advantage.objects.get().title, 'Новое преимущество')
