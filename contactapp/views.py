from django.shortcuts import render
from contactapp.models import ContactData
from contactapp.forms import Contactform
from django.http.response import HttpResponse


# Create your views here.
def Contactview(request):
    if request.method=='POST':
        cform=Contactform(request.POST)
        if cform.is_valid():
            name1=request.POST.get('name')
            salary1=request.POST.get('salary')
            email1=request.POST.get('email')
            mobile1=request.POST.get('mobile')
            location1=request.POST.get('location')

            data=ContactData(
                name='name1',
                salary='salary1',
                email='email1',
                mobile='mobile1',
                location='location1',
            )
            data.save()
            cform=Contactform()
            return render(request,'contact.html',{'abcd':cform})
        else:
            return HttpResponse('User Missing some Values')
    else:
        cform=Contactform()
        return render(request,'contact.html',{'abcd':cform})

