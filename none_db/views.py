from django.shortcuts import render_to_response


def mysite(request):
    return render_to_response('index.html')

def mysite1(request):
    return render_to_response('about_me.html')

def mysite2(request):
    return render_to_response('about_project.html')

def mysite3(request):
    return render_to_response('Ukraine.html')

def mysite4(request):
    return render_to_response('work.html')
