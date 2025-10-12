from django.db import models
from django.contrib.auth.models import User

class Disaster(models.Model):
    DISASTER_TYPES = [
        ('earthquake', 'Earthquake'),
        ('flood', 'Flood'),
        ('hurricane', 'Hurricane'),
        ('wildfire', 'Wildfire'),
        ('tornado', 'Tornado'),
        ('tsunami', 'Tsunami'),
        ('volcanic_eruption', 'Volcanic Eruption'),
        ('landslide', 'Landslide'),
        ('drought', 'Drought'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    disaster_type = models.CharField(max_length=50, choices=DISASTER_TYPES)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='disaster_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_disaster_type_display()}) - {self.location} on {self.date}"
    
class SafeZone(models.Model):
    disaster = models.ForeignKey(Disaster, related_name='safe_zones', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    capacity = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='safezone_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.latitude}, {self.longitude} (Capacity: {self.capacity})"
    
class Update(models.Model):
    disaster = models.ForeignKey(Disaster, related_name='updates', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"Update for {self.disaster.name} at {self.timestamp}"