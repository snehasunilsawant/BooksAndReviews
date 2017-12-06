# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from models import User,Book,Review

from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request,'book_app/index.html')

def register(request):
    # Users = User.objects.validate(request.POST)
    print request.POST
    user = User.objects.creator(request.POST)
    request.session['name']= user.name    
    return redirect("/")

def login(request):
    print request.POST
    results = User.objects.loginvalidation(request.POST)
    print results
    if results['status'] == False :
        messages.error(request,"Please check details. Try Again !!!")
        return redirect('/')
    request.session['email'] = results['user'].email
    request.session['name'] = results['user'].name
    request.session['id'] = results['user'].id
    return redirect('/books/')


def books(request):
    if 'email' not in request.session:
        return redirect('/')
    print request.session['id']
    user = User.objects.get(id=request.session['id'])
    otherBooks = Book.objects.exclude(users=user).values()
    userBooks = User.objects.get(id=request.session['id']).books.all()
    # Book.objects.get(id=11).have_reviews.all()
    reviews = User.objects.get(id=request.session['id']).given_review.all()
    context ={
        'otherBooks' : otherBooks,
        'userBooks' : userBooks,
        'reviews' : reviews,
    }

    return render(request,'book_app/books.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')

def add(request):
     context ={
         'authors' : Book.objects.all(),
     }  
     return render(request,'book_app/bookadd.html',context)

def addbookandreview(request):
    print request.POST
    userid = request.session['id']
    results = Book.objects.creator(request.POST,userid)
    print "book completed"
    print results['user'].name
    url = '/books/'+ str(results['book'].id)

    return redirect(url)

def bookdisplay(request,bookid):
    #show detaisl of that book id
    print bookid 
    book = Book.objects.get(id=bookid)
    context = {
        'id' : book.id,
        'title' : book.title,
        'author' : book.author,
        'rating' : book.rating,
        'review' : book.have_reviews.all(),
        'users' : book.users.all(),
    }
    return render(request,'book_app/display.html',context)
    

def userdisplay(request,userid):
    print userid
    user = User.objects.get(id=userid)
    context = {
        'name' : user.name,
        'alias' : user.alias,
        'email' : user.email,
        'reviewscount' : user.given_review.count(),
        'books' : user.books.all()
    }
    return render(request,'book_app/userdisplay.html',context)

def onlyreview(request,bookid):
    url = "/books/"+ str(bookid)
    print url
    print "inside review"
    userid = request.session['id']
    print userid

    user = User.objects.get(id=userid)

    book = Book.objects.get(id=bookid)
    
    addreview = Review.objects.create(review=request.POST['review'],reviewed_by=userid,reviews_of=bookid)
    addreview.reviews_of.rating = request.POST['rating']
    addreview.save()


    print addreview.reviews_of.rating

    return redirect(url)

    
   