from django.shortcuts import render
from models import MyData

# Create your views here.

def main(request):
    my_data = MyData.objects.first()
    return render(request, 'base.html', {'my_data' : my_data})
