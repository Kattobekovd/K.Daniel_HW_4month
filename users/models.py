from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    EXPERIENCE_CHOICES = (
        ('junior', 'junior'),
        ('middle', 'middle'),
        ('senior', 'senior'),
    )
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveSmallIntegerField(default=10,
                                           validators=[MinValueValidator(5),
                                                       MaxValueValidator(60)])
    gender = models.CharField(max_length=10, choices=GENDER)
    experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    level = models.CharField(max_length=100, default='Уровень не определен')

@receiver(post_save, sender=CustomUser)
def set_level(sender, instance, created, **kwargs):
    if created:
        print('Сигнал обработан, пользователь создан')

        experience = instance.experience
        if experience == 'junior':
            instance.experience = 'Зарплата 500$'
        elif experience == 'middle':
            instance.experience = 'Зарплата 1000$'
        elif experience == 'senior':
            instance.experience = 'Зарплата 3000$'
        else:
            instance.experience = 'Уровень не определен'
        instance.save()
