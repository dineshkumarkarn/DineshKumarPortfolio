from django.shortcuts import render
from django.http import HttpResponse
from enquiryform.models import enquiryform
from project.models import projectsdata

def homepage(request):
    data={}
    projects=projectsdata.objects.all()[:3]
    
    data={
        'project':projects
    }


    return render(request,"index.html",data)
    
    

def project(request):
    projects=projectsdata.objects.all()
    data={
        'project':projects
    }

    return render(request,"project.html",data)

def profile(request):
    return render(request,"profile.html")

def skill(request):
    return render(request,"skill.html")

def about(request):

    return render(request,"about.html")


def contact(request):
    
    data={}
    try:
        if request.method=='POST':
            # n1=int(request.GET['num1'])
            # n2=int(request.GET['num2'])
            # n1=int(request.GET.get['num1'])
            # n2=int(request.GET.get['num2'])
            name=request.POST.get('name')
            email=request.POST.get('email')
            nomber=request.POST.get('number')
            yquiry=request.POST.get('enquiry')
            
            print(name,email,nomber,yquiry)
            en=enquiryform(name=name,email=email,mobile=nomber,yenquiry=yquiry)
            en.save()
            n='your enquiry is saved i will responds you shortly'
            data={
                'n':n

                
            }
    except:
        pass

    return render(request,"form.html",data)




    