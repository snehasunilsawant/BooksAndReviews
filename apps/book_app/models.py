# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import bcrypt

# Book.objects.all().values()
# User.objects.all().values()
# Review.objects.all().values()

# Create your models here.
class BookManager(models.Manager):
    
    def creator(self,postData,userid):
        results = { 'status' : True,'errors' : [] , 'user' : None,'review' : None , 'book' : None}
        print postData
        print "inside book creator"
        print "user id is : ",userid
        if postData['author1']:
            chosenauthor = postData['author1']
        else:
            chosenauthor = postData['author2']
        print chosenauthor
        user = User.objects.get(id=userid)
        print user.name
        book = self.create(title=postData['title'],author=chosenauthor,rating=postData['rating'])
        print "book id is : ",book.id
        book.users.add(user)
        review = Review.objects.create(review=postData['review'],reviewed_by=user,reviews_of=book)
        print "review : ",Review.objects.all().values()
        print "book : ",book.users.all().values()
        print review.review
        results['user'] = user
        results['book'] = book
        results['review'] = review

        print "results", results

        return results



class UserManager(models.Manager):
    def loginvalidation(self,postData):
        results = { 'status' : True,'errors' : [] , 'user' : None}
        print "Inside login"
        users = self.filter(email = postData['email'])
        if len(users) < 1:
            results['status'] = False
        else :
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = Fals.e
        return results  

    def creator(self,postData):
        # results = { 'status' : True,'errors' : [] , 'user' : None }
        print postData
        encryptedPassword = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        user = self.create(name=postData['name'],alias=postData['alias'],email=postData['email'],password=encryptedPassword)
        print "user created"
        return user
    
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.IntegerField()
    users = models.ManyToManyField( User ,related_name ="books")
    objects = BookManager()


class Review(models.Model):
    review = models.TextField(max_length=1000)
    reviewed_by = models.ForeignKey(User , related_name="given_review")
    reviews_of = models.ForeignKey(Book , related_name="have_reviews")

