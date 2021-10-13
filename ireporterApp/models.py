from django.db import models
from django.conf import settings
def project_upload(instance, filename):
    return 'image/{}/{}'.format(instance.redflag_id, filename)
class RedFlag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='redflag', on_delete=models.CASCADE)
    title = models.CharField(max_length=43)
    description = models.TextField(max_length=100)
    status = models.CharField(max_length=20, default='received',)
    redFlag_image = models.ImageField(upload_to=project_upload, null=True, blank=True)
    redFlag_video = models.CharField(max_length=20, null=True, blank=True)
    redFlag_location = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Intervention(models.Model):
    subject = models.TextField(max_length=200)
    description = models.TextField()
    location = models.TextField(max_length=90)
    upload_image = models.ImageField(null=True)
    video =models.CharField(max_length=20, null=True, blank=True)
    save = models.TextField()       