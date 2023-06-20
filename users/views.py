from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     subject = 'Подтвердите вашу почту'
    #     message = 'Пожалуйста, нажмите на ссылку ниже, чтобы подтвердить свой адрес электронной почты:\n\n{0}'.format(
    #         self.request.build_absolute_uri(reverse_lazy('users:verify-email', kwargs={'pk': self.object.pk}))
    #     )
    #     from_email = 'noreply@example.com'
    #     recipient_list = [self.object.email]
    #     send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    #     return response


#
#
# class VerifyEmailView(View):
#     def get(self, request, pk):
#         user = User.objects.get(pk=pk)
#         user.email_verified = True
#         user.save()
#         return redirect('users:profile')

# class MyPasswordResetView(PasswordResetView):
#     email_template_name = 'users/password_reset_email.html'  # имя шаблона для отправки письма с инструкциями по
#     # восстановлению пароля
#     success_url = reverse_lazy(
#         'password_reset_done')  # URL, на который будет перенаправлен пользователь после успешной отправки письма
#     template_name = 'users/password_reset_form.html'  # имя шаблона для отображения формы восстановления пароля
