from django.shortcuts import render

# Create your views here.
def app1_sample(request):
    return render(request,'app1_sample.html')
