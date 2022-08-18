from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    MBTI_CHOICES = {
        ('ISTJ', 'istj'),
        ('ISFJ', 'isfj'),
        ('INFJ', 'infj'),
        ('INTJ', 'intj'),
        ('ISTP', 'istp'),
        ('ISFP', 'isfp'),
        ('INFP', 'infp'),
        ('INTP', 'intp'),
        ('ESTP', 'estp'),
        ('ESFP', 'esfp'),
        ('ENFP', 'enfp'),
        ('ENTP', 'entp'),
        ('ESTJ', 'estj'),
        ('ESFJ', 'esfj'),
        ('ENFJ', 'enfj'),
        ('ENTJ', 'entj'),
    }

    mbti = models.CharField(max_length=4, choices=MBTI_CHOICES, null=False)
    # 파트너 MBTI 공란 있을 경우, 디폴트 값은 solo
    mbti_partner = models.CharField(max_length=4, choices=MBTI_CHOICES, default='solo')
    mbti_keywords = models.CharField(max_length=8, null=False)