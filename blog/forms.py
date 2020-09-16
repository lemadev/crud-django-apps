from django import forms

'''
Each form field has a corresponding WIDGET class, 
which in turn corresponds to an HTML form widget 
such as <input type="text">.

attrs is a dictionary and allows us to specify some 
CSS classes
'''
class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )