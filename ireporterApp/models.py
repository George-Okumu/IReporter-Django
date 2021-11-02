from django.db import models
from django.conf import settings
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video
from django.dispatch import receiver 
from django.utils.translation import gettext_lazy as _
import geocoder
import requests
def redflag_image_upload(instance, filename):
    return 'redflag/image/{}/{}'.format(instance.id, filename)
def intervention_image_upload(instance, filename):
    return 'intervention/image/{}/{}'.format(instance.id, filename)
def redflag_video_upload(instance, filename):
    return 'redflag/video/{}/{}'.format(instance.id, filename)
mapbox_base_url='https://api.mapbox.com/geocoding/v5/mapbox.places/{}'

class RedFlag(models.Model):
    RECEIVED = 'received'
    INVESTIGATING = 'investigating'
    REJECTED = 'rejected'
    RESOLVED = 'resolved'
    IREPORTER_STATUS_CHOICES = [
        (RECEIVED, 'received'),
        (INVESTIGATING, 'investigating'),
        (REJECTED, 'rejected'),
        (RESOLVED, 'resolved'),
        
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)
    title = models.CharField(max_length=43)
    description = models.TextField(max_length=100)
    redFlag_location =models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20, choices=IREPORTER_STATUS_CHOICES, default=RECEIVED)
    redFlag_image = models.ImageField(upload_to=redflag_image_upload, null=True, blank=True)
    redFlag_video = models.FileField(upload_to=redflag_video_upload, null=True, blank=True, max_length=4000,  validators=[validate_video])    
    created_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.user.email
class Intervention(models.Model):
    RECEIVED = 'received'
    INVESTIGATING = 'investigating'
    REJECTED = 'rejected'
    RESOLVED = 'resolved'
    IREPORTER_STATUS_CHOICES = [
        (RECEIVED, 'received'),
        (INVESTIGATING, 'investigating'),
        (REJECTED, 'rejected'),
        (RESOLVED, 'resolved'),
        
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='intervention_user', on_delete=models.CASCADE)
    subject = models.TextField(max_length=200)
    description = models.TextField(max_length=100)
    status = models.CharField(max_length=20, choices=IREPORTER_STATUS_CHOICES, default=RECEIVED)
    location =models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    intervention_image = models.ImageField(upload_to=intervention_image_upload)

class Address(models.Model):
    address = models.CharField(max_length=30)
    lat = models.FloatField(blank=True, null=True)
    long =models.FloatField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.address

    
    def _search_address(self):
        
        params={
            'address':self.address,
            'access_token':settings.MAPBOX_ACCESS_TOKEN
            
        }
        search_address = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/', params)
        return search_address



   

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=settings.MAPBOX_ACCESS_TOKEN)
        g = g.latlng
        self.lat =g[0]
        self.long =g[1]
        return super(Address, self).save(*args, **kwargs)

        

