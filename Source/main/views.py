from django.shortcuts import render
from .forms import StudentRegiser
from .models import User
# Create your views here.
def Homepage(request):
    form = StudentRegiser()
    stud = User.objects.all()
    return render(request,'index.html',{'form':form,'stud':stud})


def save_file(request):
    if render.method == "POST":
        form = StudentRegiser(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            dob = request.POST['dob']
            city = request.POST['city']
            password = request.POST['password']
            user =User(name=)