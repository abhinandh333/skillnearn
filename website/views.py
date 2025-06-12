from django.shortcuts import render

# Create your views here.from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']

        context = {
            'message': message,
            'name': name,
            'email': email,
            'subject': subject,
        }

        return render(request, 'contact.html', context)


    else:
        return render(request, 'contact.html')
    
def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def joblist(request):
    return render(request, 'joblist.html')
