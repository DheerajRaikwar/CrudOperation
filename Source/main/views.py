from django.shortcuts import render
from .forms import StudentRegiser
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def Homepage(request):
    form = StudentRegiser()
    stud = User.objects.all()
    return render(request,'index.html',{'form':form,'stud':stud})

@csrf_exempt
def save_file(request):
    if request.method == "POST":
        form = StudentRegiser(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            dob = request.POST['Dob']
            city = request.POST['city']
            password = request.POST['password']
            user = User(name=name,email=email,Dob=dob,city=city,password=password)
            user.save()
            return JsonResponse({'status':'Save'})
        else:
            return JsonResponse({'status':0})