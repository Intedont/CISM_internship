from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username ')
    password = forms.CharField(label='Пароль      ')

class NewPostForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    text = forms.CharField(widget=forms.Textarea, label='Текст')

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=100, label='Комментарий')
