from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
import requests
import json
from pygments import highlight, lexers, formatters
from .forms import ReviewForm
from .models import  Review  
import statistics                                                                                  

# Create your views here
result = requests.get("https://gutendex.com/books").json()
d = {i['title']:i['id'] for i in result['results']}

def example(request):
    return render(request, 'myapp/example.html')

def index(request):
    book = request.GET['gm']
    if any(book.upper() in list(d.keys())[i].upper() for i in range(len(d.keys()))):
        BookName = [i for i in list(d.keys()) if book.upper() in i.upper()][0]
        BookId = d[str(BookName)]
        result = requests.get("https://gutendex.com/books"+"/"+str(BookId)).json()
        result = {"book":[result]}
        for x in ['translators', 'subjects', 'bookshelves','copyright', 'media_type', 'formats']:
            del result["book"][0][x]
        result = json.dumps(result, indent = 3)
        return render(request,'myapp/book.html',{'result':result}) #HttpResponse(result, content_type = "application/json")
        
def book_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            item = form.save()
            
            bk = item.bookId
            rating = item.rating
            review = item.review
            my_var = {'bk':bk,'rating':rating,'review':review}
            my_var = json.dumps(my_var,indent = 3)
            return HttpResponse(my_var,content_type="application/json")#redirect(reverse('myapp:thankyou')
        else:
            my_var = {'a':2}
            print(form.errors)
            return render(request,'myapp/review.html',context = {'form':form})
            
    else:
        form = ReviewForm()
        return render(request,'myapp/review.html',context = {'form':form})

def thankyou(request):
    #print(request.GET('csrf_token'))
    #bk = 84
    #review = Review.objects.filter(review = bk).all()
    #bookId = [c.bookId for c in review][0]
    #rating = [c.rating for c in review][0]
    #review = [c.review for c in review][0]
    #my_var = {'bookId':bookId, 'rating':rating, 'review': review}
    return render(request,'myapp/thankyou.html')

def example2(request):
    return render(request,'myapp/example2.html')

def specificbook(request):
    try:
        g = request.GET['g']
        review = Review.objects.filter(bookId=g).all()
        rating = round(statistics.mean([c.rating for c in review]),1)
        review = [c.review for c in review]
        result = requests.get("https://gutendex.com/books"+"/"+str(g)).json()
        result = {"book":[result]}
        for x in ['translators', 'subjects', 'bookshelves','copyright', 'media_type', 'formats']:
            del result["book"][0][x]
        result['rating'] = rating
        result['reviews'] = review
        result = json.dumps(result, indent = 3)
        return render(request,'myapp/combine.html',{'result':result})
    except:
        raise Http404


        
    

