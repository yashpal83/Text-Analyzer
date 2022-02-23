from django.shortcuts import render
from text.models import Contact

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        desc = request.POST.get('desc')

        contact = Contact(name = name, email = email, city = city, state = state, desc = desc)
        contact.save()           

    return render(request, 'contact.html')

def analyze(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    removenum = request.POST.get('removenum', 'off')
    capitalizefirst = request.POST.get('capitalizefirst', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')    
    charcount = request.POST.get('charcount', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    
    
    
    if text == "":
        content = {'analyzed_text': 'Please Enter some text.'}
        return render(request, 'analyze.html', content)
                
    if removenum == 'on':
        numbers = '''0123456789'''
        newtext = ""
        for char in text:
            if char not in numbers:
                newtext = newtext + char
        
        content = {'analyzed_text': newtext, 'result': 'Removed Numbers'}
        text = newtext

    if removepunc == 'on':
        punctuations = '''""|!@#$%^&*{.}?!,:;_–()[]/\‘’“”'''
        newtext = ""
        for char in text:
            if char not in punctuations:
                newtext = newtext + char
        
        content = {'analyzed_text': newtext, 'result': 'Removed Punctuations'}
        text = newtext

        # return render(request, 'analyze.html', content)
        
    if capitalizefirst == 'on':
        newtext = text.capitalize()
        
        content = {'analyzed_text': newtext, 'result': 'Capitalized First'}
        text = newtext
    
    if uppercase == 'on':
        newtext = text.upper()
        
        content = {'analyzed_text': newtext, 'result': 'TEXT IN UPPERCASE'}
        text = newtext
    
    if lowercase == "on":
        newtext = text.lower()
        
        content = {'analyzed_text': newtext, 'result': 'text in lowercase'}
        text = newtext
    
    if extraspaceremover == 'on':
        import re
        newtext = re.sub(" +", " ", text)
        
        content = {'analyzed_text': newtext, 'result': 'Extra Spaces Removed'}
        text = newtext
        # return render(request, 'analyze.html', content)

    if spaceremover == 'on':
        newtext = ""
        for char in text:
            if char != " ":
                newtext = newtext + char
    
        content = {'analyzed_text': newtext, 'result':'Spaces Removed'}
        text = newtext
        # return render(request, 'analyze.html', content)    
    
    if lineremover == 'on':
        newtext = ""
        for char in text:
            if char != "\n" and char != "\r":
                newtext = newtext + char
                                
        text = newtext           
        
        content = {'analyzed_text': newtext, 'result':'Extra Lines Removed'}
        
    if charcount == 'on':
        char = len(text)     
           
        content = {'analyzed_text': text, 'message1': 'Characters in the text are: ' + str(char)}

    
    if removepunc != "on" and removenum != "on" and capitalizefirst != "on" and uppercase != "on" and lowercase != "on" and charcount != "on" and extraspaceremover != "on" and spaceremover != "on" and lineremover != "on":

        content = {'analyzed_text': "Please Switch-on any one operation."}
        
    return render(request, 'analyze.html', content)