from django.shortcuts import render
from django.contrib import messages
import requests
# Create your views here.
IP_ADDRESS = 'http://192.168.15.11:8100' 

def Main(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        url = IP_ADDRESS+"/products?id=*&name="+name+"" 
        print('s')
    else:
        url = IP_ADDRESS+"/products?id=*&name=*"
        print('r')
    

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)


    return render(request, 'index.html', {'amount':response.json()})        

# def Amount_page(request):
    




