from django import forms
from mysite.models import notes


class NoteForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ["title",
                  "content",
                  "author",
                  "draft_staus",
                  ]
