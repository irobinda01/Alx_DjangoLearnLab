from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if '<script>' in title.lower():
            raise forms.ValidationError("Invalid input detected.")
        return title