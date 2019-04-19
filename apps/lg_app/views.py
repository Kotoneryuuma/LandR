from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
########
import bcrypt


def index(request):
    return render(request, "lg_app/index.html")

def regi(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            # if request.method == "POST":
            f_name = request.POST["fn"]
            l_name = request.POST["ln"]
            e_ma = request.POST["em"]
            p_w = request.POST["pa"]
        #######################
        # check to make sure to get information
            print(request.POST)
        ############send info to DB##########################
            hash1 = bcrypt.hashpw(p_w.encode(), bcrypt.gensalt())
            new = User.objects.create(first_name=f_name, last_name=l_name, email=e_ma, password=hash1)
            print(new)
            # ##### get last info from DB #############
            # send = User.objects.last()
            # return redirect(f'/shows/{send.id}')
            # #how to send info to 
            request.session['id'] = new.first_name
            return redirect("/success")

def login(request):
    if request.method == "POST":
        errors = User.objects.process_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            elemail = request.POST["mail_e"]
            elpas = request.POST["pass_word"]
            user =  User.objects.filter(email = elemail)
            if not user:
                messages.error(request, "Your email address doesn't exist")
                return redirect("/")
            else:
                user = User.objects.get(email=elemail)
                if bcrypt.checkpw(elpas.encode(), user.password.encode()):
                    print("password match")
                    request.session['id'] = user.first_name
                    return redirect("/success")
                else:
                    print("failed password")
                    return redirect("/")

def success(request):
    return render(request, "lg_app/success.html")


def destroy(request):
    request.session.clear()
    return redirect("/")
