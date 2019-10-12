from django.contrib.auth import login
from django.views.generic import TemplateView, FormView

from wimperg.forms import RegistrationForm


class News(TemplateView):
    template_name = 'news.html'
    extra_context = {'section': 'news'}


class Registration(FormView):
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
