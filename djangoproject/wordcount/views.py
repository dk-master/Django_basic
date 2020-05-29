from django.shortcuts import render

# Create your views here.

def home(req) :
    return render(req,'home.html')


def about(req):
    return render(req,'about.html')


def result(req):
    text = req.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1


    return render(req,'result.html', {'full': text, 'total':len(words), 'dictionary':word_dictionary.items()})