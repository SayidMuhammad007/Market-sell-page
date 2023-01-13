from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json
# from django.contrib import messages
# Create your views here.
IP_ADDRESS = 'http://127.0.0.1:8000' 
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
        break


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
        url = IP_ADDRESS+"/products?id="+id+"&name=*" 


        response = requests.request("GET", url, headers=headers, data=payload)


        return render(request, 'amount.html', {'data':response.json()})      
        

def Sell_page(request):
    url = IP_ADDRESS+"/sell?id=*"
    response = requests.request("GET", url, headers=headers, data=payload)
    all_sum = 0
    for i in response.json():
        all_sum = i['all_sum']
        break
    return render(request, 'all.html', {'data':response.json(), 'all_sum':all_sum})


def Sell_delete(request, id):
    url = IP_ADDRESS+"/sell?id="+id+""
    response = requests.request("DELETE", url, headers=headers, data=payload)
    for i in response.json():
        all_sum = i['all_sum']
        break
    return render(request, 'all.html', {'data':response.json(), 'all_sum':all_sum})

def Sell_price(request, id):
    if request.method == 'POST':
        url = IP_ADDRESS+"/sell?id="+id+""
        narx = request.POST.get('price')
        dataa = {
            'price':narx
        }
        response = requests.request("PUT", url, headers=headers, data=dataa)

        return redirect('/sell_page')
    else:
        url = IP_ADDRESS+"/sell?id="+id+""
        response = requests.request("GET", url, headers=headers, data=payload)
        return render(request, 'cost.html', {'data':response.json()})    
    
def Selled(request, type):
    tur = 'naqd'
    if type == '1':
        tur = 'plastik'
        url = IP_ADDRESS+"/selled?type="+tur+""
        response = requests.request("POST", url, headers=headers, data=payload)     
        return redirect('/')
    elif type == '2':
        tur = 'naqd'
        url = IP_ADDRESS+"/selled?type="+tur+""
        response = requests.request("POST", url, headers=headers, data=payload)     
        return redirect('/')
    elif request.method == 'POST':
        mijoz = request.POST.get('mijoz')
        print(mijoz)
        url = IP_ADDRESS+"/selled?type=nasiya&mijoz="+mijoz+""
        response = requests.request("POST", url, headers=headers, data={'mijoz':mijoz})     
        return redirect('/')



def Customer_page(request):
    url = IP_ADDRESS+"/customer"
    response = requests.request("GET", url, headers=headers, data=payload)         
    return render(request, 'customer.html', {'customers':response.json()})

def Customer_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        payload1 = {
            "name": name,
            "phone": phone,
            "comment": comment
        }
        url = IP_ADDRESS+"/customer"
        response = requests.request("POST", url, headers=headers, data=payload1)         
        return redirect('/nasiya')
    else:
        return render(request, 'customer_add.html')