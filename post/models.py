from django.db import models
from user.models import User

class Post(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, verbose_name="사용자")
    content = models.TextField("포스팅내용", null=True)
    def __str__(self):
        return f'{self.user}의 포스팅'