from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    data = request.GET['tarea']
    word_list=data.split()
    list_length=len(word_list)
    return render(request,'count.html', {'fulltext':data,'words':list_length})



  