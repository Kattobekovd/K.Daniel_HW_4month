from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import models, middlewares, forms

class RegistrationView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'users/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        experience = form.cleaned_data['experience']
        if experience == 'junior':
            self.object.level = 'Зарплата 500$'
        elif experience == 'middle':
            self.object.level = 'Зарплата 1000$'
        elif experience == 'senior':
            self.object.level = 'Зарплата 3000$'
        else:
            self.object.level = 'Уровень не определен'
        self.object.save()
        return response

class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse('users:user_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['level'] = getattr(self.request, 'level', 'Уровень не определен'),
        return context






