from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
import jwt
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('User must have a username.')

        if email is None:
            raise TypeError('User must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.save()
        return user
  
class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    email = models.EmailField(unique=True, db_index=True)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    is_email_verified = models.BooleanField(default=False)
    class Types(models.TextChoices):
        ADMIN="ADMIN", "Admin"
        USER="USER", "User"
    userType = models.CharField(_("userType"), max_length=30, choices=Types.choices, default=Types.USER)
    @property
    def token(self):
        return self._generate_jwt_token()
    EMAIL_FIELD ='email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email

    

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

 
    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=30)
        token = jwt.encode({
            'username':self.username,
            'id': self.pk,
            'exp': int(dt.strftime('%s')),
            'email':self.email,
            'userType':self.userType
        }, settings.SECRET_KEY, algorithm='HS256')
        return token
# class AdminManager(models.Manager):
    # def create_admin(self, username, email, password=None):
    #     if email is None:
    #         raise TypeError("Valid email address is required")
    #     admin = self.model(username=username, email=self.normalize_email(email))
    #     admin.set_password(password)
    #     admin.save()
    #     return admin
    # def get_queryset(self, *args, **kwargs):
    #     return super().get_queryset(*args, **kwargs).filter(userType = CustomUser.Types.ADMIN)

class Admin(CustomUser):

    class meta:

        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.userType = CustomUser.Types.ADMIN
            self.set_password(self.password)
            self.email = self.email
        super(Admin, self).save(*args, **kwargs)
        
        