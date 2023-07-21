from django.db import models

class User(models.Model):
  openid = models.CharField(max_length=50)
  # 其他用户字段