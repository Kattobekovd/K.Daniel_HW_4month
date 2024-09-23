from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
EXPERIENCE_CHOICES = (
        ('junior', 'junior'),
        ('middle', 'middle'),
        ('senior', 'senior'),
    )

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    experience = forms.ChoiceField(choices=EXPERIENCE_CHOICES, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'experience',
        )
    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

@receiver(post_save, sender=models.CustomUser)
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















