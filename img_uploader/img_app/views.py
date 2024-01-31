from django.shortcuts import render,HttpResponse
from .forms import ImageForm
from .models import Image

def home(request):
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            
    form = ImageForm()
    
    return render(request,'home.html',{'form':form})

def view_img(request):
    
    imgs = Image.objects.all()
    
    
    return render(request,'all_img.html',{'imgs':imgs})