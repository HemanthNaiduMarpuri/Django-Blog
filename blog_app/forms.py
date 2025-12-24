from django import forms
from .models import User, Blog, Comment
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, AuthenticationForm

class UserCreationForm(BaseUserCreationForm):
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    password2 = forms.CharField(
        label='confirm password',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']