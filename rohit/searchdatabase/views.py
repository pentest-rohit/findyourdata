from django.shortcuts import render
from .models import SearchData

# Create your views here.

def home(request):
    return render(request, 'index.html')

def search(request):
    if request.method=='POST':
        phone = request.POST.get('phone')
        user = SearchData.objects.filter(phone=phone)
        context = {'user' : user}
        return render(request, 'search.html', context)
