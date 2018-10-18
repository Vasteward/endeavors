from django.shortcuts import render, redirect, HttpResponse
from .models import *
import re
import bcrypt
from django.contrib import messages
from django.contrib.auth import logout
from django.conf import settings
from datetime import datetime
from django.db.models import Q
from django.shortcuts import render
from datetime import date, time, datetime
from time import gmtime, strftime, localtime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
def index(request):
    return render(request, 'exam/index.html')
#process
def register(request):
    #validations
    if request.method != "POST":
        return redirect('/')
    error = False
    if len(request.POST['first']) < 3:
        print('First name must be longer than 3 characters')
        messages.error(request, 'First name must be longer than 3 characters')
        error = True
    if len(request.POST['last']) < 3:
        print('Last name must be longer than 3 characters')
        messages.error(request, 'Last name must be longer than 3 characters')
        error = True
    if not request.POST['first'].isalpha() or not request.POST['last'].isalpha():
        print("First and Last name must only contain letters")
        messages.error(request, "First and Last name must only contain letters")
        error=True
    if not EMAIL_REGEX.match(request.POST['email']):
        print("Email is invalid")
        messages.error(request, "INVALID EMAIL!")
        error=True
    if request.POST['pw'] != request.POST['confirm_pw']:
        print("Passwords don't match")
        messages.error(request, "Passwords don't MATCH!")
        error=True
    if len(request.POST['pw']) < 8:
        print("Password is too short")
        messages.error(request, "Password must be longer than 8 characters")
        error=True
    if User.objects.filter(email = request.POST['email']):
        messages.error(request, "Proceed to login.")
        print("user is already in the database")
        error=True
    if error:
        print("WE HAVE ERRORS")
        return redirect('/')
    else: 
        hashed = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
        #if good, hash pw
        #store in db
        #generate error msgs
        newUser = User.objects.create(first_name = request.POST['first'], last_name=request.POST['last'], email=request.POST['email'], password=hashed)
        request.session['user_id'] = newUser.id
        print("SUCCESS")
        request.session['greeting'] = "Glad you signed up!"
        return redirect('/success')

def validate_login(request):
    print(User.objects.all().values())
    if request.method != "POST":
        return redirect('/')
    #validations
    #check if user is in db
    #generate error msgs
    user = User.objects.filter(email=request.POST['email'])

    if len(user) > 0:
        print("THERE'S SOMETHING HERE")
        #if the email is in the db, decrypt the password and check if it is the same as what is stored
        if bcrypt.checkpw(request.POST['pw'].encode(), user[0].password.encode()):
            print('password match')
            #put the person in session, the user[0] is the first person in the list, grabbing the id and put it in session 
            request.session['user_id'] = user[0].id
            request.session['greeting'] = "Welcome "
            #redirect to the success page
            return redirect('/success')
        else: 
            #flash, password doesn't match
            print(user[0].password.encode())
            print("password does not match")
            messages.error(request, "Invalid Credentials")
            return redirect('/')
    else:
        # redirect to registration and send message
        print("The person is a newb.")
        messages.error(request, "Welcome new user. Please, register.")
        print("BATMAN"*20)
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    # Fetch records from db
    # create a dictionary to pass to the browser
    if not 'user_id' in request.session:
        return redirect('/')
    context={
        "user": User.objects.get(id=request.session['user_id']),
        "job": Job.objects.all(),
        "users_jobs": User.objects.get(id=request.session['user_id']).created_job.all()
    }
    return render(request, 'exam/dashboard.html', context)

#RENDER_________________________________________________________

def add(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = { "date": strftime("%b %d, %Y", localtime()), "time": strftime("%I:%M %p", localtime())}
    print('\n\n'*5)
    print(context)
    print('\n\n'*5)
    return render(request, 'exam/add.html', context)

def edit(request, job_id):
    # Fetch records from db
    # create a dictionary to pass to the browser
    if not 'user_id' in request.session:
        return redirect('/')
    context={
        'job': Job.objects.get(id=job_id),
    }
    return render(request, 'exam/edit.html', context)

def show(request, job_id):
    if not 'user_id' in request.session:
        return redirect('/')
    #need context to show information on the page
    context={
        "particular_job": Job.objects.get(id=job_id)
    }
    return render(request, 'exam/show.html', context)


#PROCESSES_________________________________________________________

def create_process(request):
    #security
    if request.method != "POST":
        return redirect('/')
    if not 'user_id' in request.session:
        return redirect('/')
    #validations
    error=False
    if len(request.POST['title']) < 3:
        print('Destination must be longer than 3 characters')
        messages.error(request, 'Title must be longer than 3 characters')
        print("@"*50)
        error=True
    if len(request.POST['description']) < 10:
        print('Description name must be longer than 10 characters')
        print("SUPER"*20)
        messages.error(request, 'Description must be longer than 10 characters and do not use slashes')
        error=True
    if request.POST['location'] == "" :
        print('Something went awry')
        print("\n\n")
        messages.error(request, "Location must not be left blank")
        error=True
    if error:
        return redirect('/add')
    #create query and attach to user
    Job.objects.create(title=request.POST['title'], description=request.POST['description'], location=request.POST['location'], creator_id=request.session['user_id'])
    return redirect('/success')


def update(request, job_id):
    if request.method != "POST":
        return redirect('/success')
    #validations
    error=False
    if len(request.POST['title']) < 3:
        print('Destination must be longer than 3 characters')
        messages.error(request, 'Title must be longer than 3 characters')
        print("@"*50)
        error=True
    if len(request.POST['description']) < 10:
        print('Description name must be longer than 10 characters')
        print("SUPER"*20)
        messages.error(request, 'Description must be longer than 10 characters and do not use slashes')
        error=True
    if request.POST['location'] == "" :
        print('Something went awry')
        print("\n\n")
        messages.error(request, "Location must not be left blank")
        error=True
    if error:
        return redirect('/add')
    change=Job.objects.get(id=job_id)
    change.title=request.POST['title']
    change.save()
    print(request.POST['title'])
    change.description= request.POST['description']
    print(request.POST['description'])
    change.save()
    change.location= request.POST['location']
    change.save()
    print(request.POST['location'])
    return redirect("/success")

# def users_job(request, job_id):
#     job = Job.objects.get(id=job_id)

#     worker = User.objects.get(id=job_id)
#     job.objects.add(worker)
#     # Job.objects.get(id=job_id).creator.add(request.session['user_id'])

#     return redirect('/success')


#TARGETED ACTIONS_______________________________________
def cancel(request, job_id):
    Trip.objects.get(id=trip_id).travelers.remove(request.session['user_id'])
    return redirect('/success')

def destroy(request, job_id):
    if not 'user_id' in request.session:
        return redirect('/success')
    job = Job.objects.get(id=job_id)
    if job.creator.id == request.session['user_id']:
        job.delete()
    return redirect('/success')