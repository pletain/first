from django.shortcuts import render

# Create your views here.


def pop(request):
    return render(request, 'quiz/pop.html')
