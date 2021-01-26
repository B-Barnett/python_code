from django.shortcuts import render
import datetime
# from time import gmtime, strftime

# def time(request):
#     context = {
#         "time":strftime("%Y-%m-%d %I:%H %p", gmtime())
#     }
#     return render(request,'index.html', context)

def time(request):
    mydate = datetime.datetime.now()
    context = {
        'mydate' : mydate
    }
    return render(request, 'index.html', context)