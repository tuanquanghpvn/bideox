from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse_lazy, reverse
from django.apps import apps as django_apps
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (
    CreateView, FormView,
)
from django.contrib.auth.forms import (
        UserCreationForm,
        AuthenticationForm,
)

from apps.core.views import BaseView

class SignupUserView(BaseView, CreateView):
    model = django_apps.get_model(settings.AUTH_USER_MODEL)
    form_class = UserCreationForm
    template_name = 'users/signup.html'

    def get_success_url(self):
        return reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(SignupUserView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Signup'
            }
        }
        context.update(info)
        return context

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "You've signed up successfully,\
                            You can log in now.")
        return HttpResponseRedirect(self.get_success_url())

class LoginUserView(BaseView, FormView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', False)
        info = {
            'info': {
                'title': 'Login'
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        nextlink = self.request.POST.get('next', False)
        if nextlink:
            return nextlink
        return reverse_lazy('posts:index')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)