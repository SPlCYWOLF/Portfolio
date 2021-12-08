from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 11/21 유저 필드에 정보 채워넣어주기 위해 수정
    age = models.IntegerField(default=10)
    preference = models.IntegerField(default=28)
    
