from django.shortcuts import render

# Create your views here.
def vote(request):
    d ={'name':'Ranjitha' ,'age':23}
    return render(request,'vote.html',context=d)
