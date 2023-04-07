from django.shortcuts import HttpResponse , render , redirect 
from .models import UserDetails
from .form import DataForm


# Create your views here.
def name(request):
    return HttpResponse ("<h1>Diversified</h1>",)
def index(request):
    return render(request,"index.html")
def demo(request):
    return render(request,'demoindex.html')  
def create(request):
    form = DataForm()
    if request.method == "POST" :
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/retrieve")
        # name = request.POST['name']
        # email = request.POST['email']
        # city = request.POST['city']
        # pincode = request.POST['pincode']
        # message = request.POST['message']
        # password = request.POST['password']
        # obj = UserDetails.objects.create(name=name, email=email, city=city,pincode=pincode, message=message, password=password)
        # obj.save()
        
        # return redirect("/retrieve")
    
    return render(request,"index.html" , {"form":form})

def retrieve(request):
    details=UserDetails.objects.all() 
    return render(request,'retrieve.html',{'details':details})
def delete(request , id):
    details=UserDetails.objects.get(id=id)
    details.delete()
    return redirect("/retrieve")
def editDetails(request, id):
    details = UserDetails.objects.get(id=id)
    return render(request,"edit.html", {'details':details})
def update (request , id):
    details = UserDetails.objects.get(id=id)
    if request.method == "POST" :
        details.name = request.POST['name']
        details.email = request.POST['email']
        details.city = request.POST['city']
        details.pincode = request.POST['pincode']
        details.message = request.POST['message']
        details.password = request.POST['password']
        details.save()
        return redirect ("/retrieve")
        
        


    
    


