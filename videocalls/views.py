from django.shortcuts import render, get_object_or_404, redirect
from .models import Videocall
import requests
import environ
from time import sleep
from threading import Thread

def videocall_index_view(request):
    queryset = Videocall.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "videocall/index.html", context)

def videocall_create():
    env = environ.Env()
    environ.Env.read_env()
    ip = env('DIRECCION_IP')
    sleep(1)
    req = requests.get(f'http://{ip}:3000/API')
    link = f"http://{ip}:3000/" + str(req.content).replace("b", "", 1).strip("'")

    new_call = Videocall(url=link)
    new_call.save()

def videocall_middleware(request):
    env = environ.Env()
    environ.Env.read_env()
    ip = env('DIRECCION_IP')
    create = Thread(target=videocall_create)
    create.start()
    return redirect(f'http://{ip}:3000')

def videocall_delete(request, data):
    obj = Videocall.objects.get(pk=data)
    url = obj.url
    obj.delete()
    return redirect(url)
