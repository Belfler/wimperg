from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib import messages

from images.models import Image
from images.forms import ImageCreateForm


class CreateImage(CreateView):
    model = Image
    template_name = 'image/create.html'
    form_class = ImageCreateForm
    extra_context = {'section': 'images'}

    def get_form(self, form_class=None):
        return self.form_class(data=self.request.GET)

    def form_valid(self, form):
        image = form.save(commit=False)
        image.author = self.request.user
        image.save()
        messages.success(self.request, 'Image added successfully')
        return redirect(image.get_absolute_url())
