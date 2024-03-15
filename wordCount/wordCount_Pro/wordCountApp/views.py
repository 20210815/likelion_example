from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "index.html")

def wordCount(request):
  return render(request, "wordCount.html")


def result(request):
  entered_text = request.GET['fulltext']

  character_count = len(entered_text)
  excluding_spaces = len(entered_text.replace(' ', '')) #3번 


  word_list = entered_text.split()

  word_count = len(word_list) #1번

  word_dictionary = {}

  for word in word_list:
    if word in word_dictionary:
      word_dictionary[word] += 1
    else:
      word_dictionary[word] = 1

  return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'wordCount': word_count, 'c_count': character_count, 'ex_space': excluding_spaces})



def hello(request):
  name = request.GET['myname']

  return render(request, "hello.html", {'name': name})