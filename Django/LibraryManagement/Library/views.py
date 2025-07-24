from django.shortcuts import render
def Home(request):
    return render(request,'index.html')
def Books(request):
    return render(request,'Books.html')
def Members(request):
    return render(request,'Members.html')
def IssueBook(request):
    return render(request,'IssueBook.html')
def ReturnBook(request):
    return render(request,'ReturnBook.html')
def Contactus(request):
    return render(request,'Contactus.html')
# Create your views here.
