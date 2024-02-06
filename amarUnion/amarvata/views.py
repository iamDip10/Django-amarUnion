from django.shortcuts import render
from django.shortcuts import redirect
from .models import *

# Create your views here.

def landingPage(req):
    return render(req, "home.html")

def signuprender(req):
    return render (req, "signup.html")

def storeuser(req):

    if req.method == 'POST':
        name = req.POST['name']
        per_add = req.POST['per_add']
        pres_add = req.POST['pres_add']
        number = req.POST['number']
        nid = req.POST['nid_number']
        passs = req.POST['pass']
        conf_passs = req.POST['conf_pass']

        if passs==conf_passs:
            print("Hello")
            users = user(name=name, per_add=per_add, press_add=pres_add, mobile=number, nid_number=nid, password=passs)
            users.save()

    return redirect ("dashb")

def dashboard(req):
    return render (req, "dashboard.html")