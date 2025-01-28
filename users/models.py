from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES=(
        ('instructor','Instructor'),
        ('admin','Admin'),
        ('student','Student')
    )
    id= models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True)
    role=models.CharField(max_length=255,choices=ROLE_CHOICES)
