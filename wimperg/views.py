from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from wimperg.models import Profile
from wimperg.forms import RegistrationForm, EditUserForm, EditProfileForm


class News(TemplateView):
    template_name = 'news.html'
    extra_context = {'section': 'news'}


class Registration(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('wimperg:index')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return super().form_valid(form)


class ChangingProfile(TemplateView):
    template_name = 'edit.html'

    def post(self, request, *args, **kwargs):
        user_form = EditUserForm(instance=request.user, data=request.POST)
        profile_form = EditProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Changes have been successfully saved.')
        else:
            messages.error(request, 'Some error has occurred.')
        return render(self.request, self.template_name, context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = EditUserForm(instance=self.request.user)
        context['profile_form'] = EditProfileForm(instance=self.request.user.profile)
        return context
