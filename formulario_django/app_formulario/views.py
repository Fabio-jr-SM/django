from django.shortcuts import render
from django.http import HttpResponseRedirect

def feed(request):
    
    context = {
        'posts' : [
            {'autor':'Riana','content':'kpcacpakscaopckapockaspkpcacpakscaopckapockaspefwfwefwefwefwfwfwecoakcspokcoapsckefwfwefwefwefwfwfwecoakcspokcoapsck','date':'12/12/2033','img':'person-circle.svg'},
            {'autor':'Fabio','content':'kpcacpakscaopckapockkpcacpakscaopckapockaspefwfwefwefwefwfwfwecoakcspokcoapsckaspcoakcspokcoapsck','date':'12/12/2033','img':'/riana.webp'},
            {'autor':'Fabio','content':'kpcacpakscaopckapockaskpcacpakscaopckapockaspkpcacpakscaopckapockaspefwfwefwefwefwfkpcoakcspokcoapsck','date':'12/12/2033','img':'/riana.webp'},
        ]
    }
    
    return render(request,'feed.html',context)

def publicate(request):
    
    if request.method == 'POST':
        autor = request.POST.get("author")
        content = request.POST.get("content")
        
        print(autor)
        print(content)
        return HttpResponseRedirect('/feed')
    else:
        return render(request,'publicate.html')