from django import forms
from .models import UserModel ,PostModel , LikeModel , CommentModel

"""
class to open sign up form
"""

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email','username','name','password']


'''
class to open Login form
'''

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

'''
class to open PostForm 
'''

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["image" , "caption"]

'''
class to open Like form
'''

class LikeForm(forms.ModelForm):
    class Meta:
        model = LikeModel
        fields=['post']

'''
class to open Comment Form 
'''

class CommentForm(forms.ModelForm):
  class Meta:
    model = CommentModel
    fields = ['comment_text', 'post']