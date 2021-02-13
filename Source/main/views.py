from django.shortcuts import render
from .forms import StudentRegiser
from .models import User
# Create your views here.
def Homepage(request):
    form = StudentRegiser()
    stud = User.objects.all()
    return render(request,'index.html',{'form':form,'stud':stud})
