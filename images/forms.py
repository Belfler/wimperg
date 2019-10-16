from urllib import request

from django import forms

from images.models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.HiddenInput}

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(f'File extension {extension} is not supported.')
        return url

    def save(self, commit=True, *args, **kwargs):
        image = super().save(commit=False)
        url = self.cleaned_data['url']
        extension = url.rsplit('.', 1)[1].lower()
        file_name = f"{slugify(image.title)}.{extension}"
        response = request.urlopen(url)
        image.image.save(name=file_name, content=ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image
