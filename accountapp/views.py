from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})


# 요청을 받은 객체 안에서 method를 찾고 post일 경우 기존 render 방식 쓰는데 추가적으로 안에다가 context라는 데이터꾸러미 안에 text이름을 가진 POST METHOD라는 문장을 넣어서 리턴


