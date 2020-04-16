from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render

# Create your views here.

class Another(View):
    #books = Book.objects.all()
    books = Book.objects.filter(is_published = False)
    output = ''
    for book in books:
        output += f"we have {book.title} in the database"
    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')

def template(request):
    return render (request, 'first_temp.html')
