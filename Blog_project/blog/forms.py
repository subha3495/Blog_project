from django import forms
from blog.models import Comment
class EmailSendForm(forms.Form):
    name       = forms.CharField()
    email_form = forms.EmailField()
    email_to   = forms.EmailField()
    comments   = forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.Form):
    class Meta:
        models = Comment
        fields = ('name','body','email')