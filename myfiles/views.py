from django.shortcuts import render, redirect
from django.contrib import messages
import requests

# from django.contrib import messages
# Create your views here.
IP_ADDRESS = 'http://192.168.88.94:8002' 
payload = ""
headers = {}

def Main(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        url = IP_ADDRESS+"/products?id=*&name="+name+"" 

    else:
        url = IP_ADDRESS+"/products?id=*&name=*"

    response = requests.request("GET", url, headers=headers, data=payload)
    for i in response.json():
        o = (i['all_pro'])


    return render(request, 'index.html', {'amount':response.json(), 'o':o})        

def Amount_page(request, id):
    if request.method == 'POST':
        miqdor = request.POST.get('amount')
        url = IP_ADDRESS+"/products?id="+id+"&amount="+miqdor+""


        response = requests.request("PATCH", url, headers=headers, data=payload) 
        a =  response.json()
        if a['status'] == 'False':
            url = IP_ADDRESS+"/products?id="+id+"&name=*" 

            response = requests.request("GET", url, headers=headers, data=payload)
            messages.error(request, "Omborda buncha mahsulot yo`q!!!")
            return render(request, 'amount.html', {'data':response.json()}) 
        else:
            return redirect('/') 
        
    else:
        print('elsega kirdi')
        url = IP_ADDRESS+"/products?id="+id+"&name=*" 


        response = requests.request("GET", url, headers=headers, data=payload)


        return render(request, 'amount.html', {'data':response.json()})      
        

def Sell_page(request):
    url = IP_ADDRESS+"/sell"


    response = requests.request("GET", url, headers=headers, data=payload)
    return render(request, 'all.html', {'data':response.json()})


def Sell_delete(request, id):
    url = IP_ADDRESS+"/sell?id="+id+""

    response = requests.request("DELETE", url, headers=headers, data=payload)
    
    return render(request, 'all.html', {'data':response.json()})
    
