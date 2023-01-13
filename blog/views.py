from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
def aa_page(request):
    return render(
        request,
        'blog/aa.html',)
def bb_page(request):
    return render(
        request,
        'blog/bb.html',)
def hansua_page(request):
    return render(
        request,
        'blog/hansua.html',)
def mbti_page(request):
    return render(
        request,
        'blog/hansua/mbti.html',)
def jihyun_page(request):
    return render(
        request,
        'blog/jihyun.html',)

def limdoyoung_page(request):
    return render(
        request,
        'blog/limdoyoung.html',)