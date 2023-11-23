import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .models import User

def error404(request, exception):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')

def handle_uploaded_file(f):
    with open("uploaded_files.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def api_upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["files"])
            return HttpResponseRedirect("/success")
        else:
            print(form.errors)
            return render(request, "upload.html", { "form_msg": form.errors })
    else:
        form = UploadFileForm()
    return render(request, "upload.html")


@csrf_exempt
def api_update_profpic(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            # Loop through multiple files (if multiple files are allowed)
            for file in reversed(request.FILES.getlist('files')):
                # Save each file as the new profile picture for the user
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = User.objects.filter(username=username, password=password)

                if user:
                    user.profpic = file
                    user.save()

            response = {"status": True, "message": "Profile picture(s) updated successfully"}
            return HttpResponse(json.dumps(response))
        else:
            response = {"status": False, "message": "Invalid form data"}
            return HttpResponse(json.dumps(response))

@csrf_exempt
def api_create(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            profpic = form.cleaned_data['files']
            
            if not username or not profpic:
                response = {"status": False}
                return HttpResponse(json.dumps(response))
            
            if User.objects.filter(username=username).exists():
                response = {"status": False}
                return HttpResponse(json.dumps(response))
            
            # Create user with profile picture
            User.objects.create(username=username, password=password, profpic=profpic)
            
            # Everything went right
            return HttpResponseRedirect("/success")
        else:
            response = {"status": False}
            return HttpResponse(json.dumps(response))
    
    else:
        response = {"status": False}
        return HttpResponse(json.dumps(response))

def upload_form(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the form submission if needed
            pass
    else:
        form = UploadFileForm()
    
    return render(request, "upload.html", { "form": form })

def show_create(request):
    return render(request, 'create.html')

def show_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = User.objects.filter(username=username, password=password)
        
        if check_user:
            request.session['user'] = username
            request.session['password'] = password
            return HttpResponseRedirect('/dashboard')

        else:
            return render(request, 'loginerr.html')

    return render(request, 'login.html')

def show_update(request):
    if 'user' and 'password' in request.session:
        username = request.session['user']
        password = request.session['password']
       
        params = { "username": username, "password": password }
        return render(request, 'update_profpic.html', params)
    else:
        return HttpResponseRedirect('/login')

def show_upload(request):
    return render(request, 'upload.html')

def show_index(request):
    return render(request, 'index.html')

def show_success(request):
    return render(request, 'success.html')