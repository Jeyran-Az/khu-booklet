from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
   if request.method== 'POST': 
     form= UserCreationForm()
   else:
     form= UserCreationForm(request.POST)
     if form.is_valid():
       new_user= form.save()
       login(request, new_user)
       return redirect('BookletApp:index')
   context= {"form":form}  
   return render(request,'registration/register.html',context)