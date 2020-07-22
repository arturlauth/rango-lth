from django import forms
from django.forms import TextInput

from rango.rangomain.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    titulo = forms.CharField(max_length=128,
                             help_text="Please enter the page name.")
    url = forms.URLField(max_length=200,
                         help_text="please enter the URL of the page",
                         widget=TextInput)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    category = forms.ModelChoiceField(queryset=Category.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url += 'http://'
            cleaned_data['url'] = url

        return self.cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        fields = ('titulo', 'url', 'views', 'category')
