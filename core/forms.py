from django import forms
from core.models import Book

class TopicSearch(forms.Form):
    pass
    # topic = forms.MultipleChoiceField(
    #     widget=forms.widgets.CheckboxSelectMultiple,
    #     label="Topics",
    #     choices=Book.topic_choices,
    #     required=False)

    # def search(self):

    #     data = self.cleaned_data['topic']
    #     books = Book.objects.all()

    #     books = books.filter(topics=data)
    #     return books
