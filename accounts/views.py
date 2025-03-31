from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')