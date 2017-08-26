# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4
# Create your models here.
'''
This model is use to store user information
'''

class UserModel(models.Model):

    email = models.EmailField(max_length= 254 , default = 'Null')
    name = models.CharField(max_length = 120 ,  default = 'Null')
    username = models.CharField(max_length = 120, default = 'Null')
    password = models.CharField(max_length= 40, default = 'Null')
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "<UserModel : %s - %s>" % (self.username, self.id)

'''
This model is use to store session token 
'''

class SessionToken(models.Model):
    user = models.ForeignKey(UserModel)
    session_token = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = str(uuid4())

'''
This model is use to store user information of uploaded post
'''

class PostModel(models.Model):
    user = models.ForeignKey(UserModel)
    image = models.FileField(upload_to='user_images')
    image_url = models.CharField(max_length=255)
    caption = models.CharField(max_length=240)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def like_count(self):
        return self.likemodel_set.count()

    @property
    def comments(self):
        return self.commentmodel_set.order_by("created_on").all()

    def liked_by_user(self, user):
        l = self.likemodel_set.filter(user=user)
        return len(l) > 0

'''
This model is use to store the post id and the user who liked it of the post
'''

class LikeModel(models.Model):
    user = models.ForeignKey(UserModel)
    post = models.ForeignKey(PostModel)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

'''
This model is use to store the post id and the user who commented on  the post
'''

class CommentModel(models.Model):
    user = models.ForeignKey(UserModel)
    post = models.ForeignKey(PostModel)
    comment_text = models.CharField(max_length=555)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)