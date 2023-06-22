from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.

# class RegisterView(CreateView):
#     model = User
#     form_class = UserRegisterForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('register_done')
        return render(request, 'users/register.html', {'form': form})


class RegisterDoneView(View):
    def get(self, request):
        return render(request, 'users/register_done.html')


class VerifyEmailView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_verified = True
        user.save()
        login(request, user)
        return redirect('home')
