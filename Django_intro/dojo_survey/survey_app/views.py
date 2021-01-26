from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, "index.html")

#Process the form and display the form data
def result(request):
    print(request.POST)
    #'your_name' gets pulled from the input in index.html
    #'name' is a new variable assigned to then use wherever
    request.session['name'] = request.POST['your_name']
    request.session['location'] = request.POST['dojos']
    request.session['language'] = request.POST['languages']
    # redirects to the display path once the form is submitted
    return redirect("/display")

def display(request):
    # recieves the redirect and renders the results.html
    return render(request, "result.html")