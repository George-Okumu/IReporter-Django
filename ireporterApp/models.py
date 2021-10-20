from django.db import models
from django.conf import settings
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video
from django.dispatch import receiver 
def redflag_image_upload(instance, filename):
    return 'redflag/image/{}/{}'.format(instance.id, filename)
def intervention_image_upload(instance, filename):
    return 'intervention/image/{}/{}'.format(instance.id, filename)
def redflag_video_upload(instance, filename):
    return 'redflag/video/{}/{}'.format(instance.id, filename)
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
    status = models.CharField(max_length=20, choices=IREPORTER_STATUS_CHOICES, default=RECEIVED)
    redFlag_image = models.ImageField(upload_to=redflag_image_upload)
    redFlag_video = models.FileField(upload_to=redflag_video_upload, null=True, blank=True, max_length=4000, storage=VideoMediaCloudinaryStorage(), validators=[validate_video])
    redFlag_location = models.CharField(max_length=20, null=True, blank=True)
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
    location = models.TextField(max_length=90)
    intervention_image = models.ImageField(upload_to=intervention_image_upload)
