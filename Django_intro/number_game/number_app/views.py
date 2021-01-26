from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    request.session['number'] = random.randint(1, 100)
    print(request.session['number'])
    return render(request, "index.html")

#IT WORKS
def result(request):
    user_guess = request.POST['user_number']
    user_guess = int(user_guess)
    context = {
        'user_guess' : user_guess
    }
    return render(request, "index.html", context)

#handles the user form
# def result(request):
#     request.session['users_number'] = request.POST['user_number']
#     print(request.session['users_number'])
#     guess = int(request.session['users_number'])
#     request.session['guess'] = guess
#     return redirect('/show')

# def show(request):
#     del request.session['guess']
#     return render(request, "index.html")
