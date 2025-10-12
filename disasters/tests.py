from django.test import TestCase
from django.contrib.auth.models import User
from .models import Disaster, SafeZone, Update

class DisasterModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.disaster = Disaster.objects.create(
            name='Test Earthquake',
            disaster_type='earthquake',
            description='A test earthquake',
            location='Test Location',
            date='2023-01-01',
            created_by=self.user
        )

    def test_disaster_creation(self):
        self.assertEqual(self.disaster.name, 'Test Earthquake')
        self.assertEqual(self.disaster.disaster_type, 'earthquake')
        self.assertEqual(self.disaster.description, 'A test earthquake')
        self.assertEqual(self.disaster.location, 'Test Location')
        self.assertEqual(str(self.disaster), 'Test Earthquake (Earthquake) - Test Location on 2023-01-01')
        
class SafeZoneModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.disaster = Disaster.objects.create(
            name='Test Flood',
            disaster_type='flood',
            description='A test flood',
            location='Test Location',
            date='2023-01-01',
            created_by=self.user
        )
        self.safezone = SafeZone.objects.create(
            disaster=self.disaster,
            name='Test Safe Zone',
            latitude=12.34,
            longitude=56.78,
            capacity=100,
            description='A test safe zone'
        )

    def test_safezone_creation(self):
        self.assertEqual(self.safezone.name, 'Test Safe Zone')
        self.assertEqual(self.safezone.latitude, 12.34)
        self.assertEqual(self.safezone.longitude, 56.78)
        self.assertEqual(self.safezone.capacity, 100)
        self.assertEqual(str(self.safezone), 'Test Safe Zone - 12.34, 56.78 (Capacity: 100)')
        
class UpdateModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.disaster = Disaster.objects.create(
            name='Test Hurricane',
            disaster_type='hurricane',
            description='A test hurricane',
            location='Test Location',
            date='2023-01-01',
            created_by=self.user
        )
        self.update = Update.objects.create(
            disaster=self.disaster,
            author=self.user,
            message='This is a test update.'
        )

    def test_update_creation(self):
        self.assertEqual(self.update.disaster, self.disaster)
        self.assertEqual(self.update.author, self.user)
        self.assertEqual(self.update.message, 'This is a test update.')
        self.assertIn('Update for Test Hurricane at', str(self.update))