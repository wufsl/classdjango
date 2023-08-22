from django.db import models

# Create your models here.

# class 하나가 db에서 아이템 하나가 됨.
# model 상속받아서 쓸건데 model 소스 코드 기초적인 모델을 가져와서 여기서 원하는 추가 정보를 입력하고 그것을 새로운 클래스 모델로 만드는 것
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
