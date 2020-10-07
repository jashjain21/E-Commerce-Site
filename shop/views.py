from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders
from math import ceil
# Create your views here.
def index(request):
    #products=Product.objects.all()
    # print(products)
    # n=len(products)
    # nSlides=n//4 + ceil((n/4)-(n//4))

    # params={'no_of_product':nSlides,'range':range(1,nSlides),'product':products}
    # allProds=[[products,range(1,nSlides),nSlides],
    #             [products,range(1,nSlides),nSlides],]
    allProds=[]
    catProds=Product.objects.values('category','id')
#     catProds is <QuerySet [{'category': 'Fashion', 'id': 6}, {'category': 'Clothing', 'id': 7}, {'category': 'Electronics', 'id': 8}, {'category': 'Home Appliances', 'id': 9}, {'category': 'Phone
# s', 'id': 10}, {'category': 'Shoes', 'id': 11}, {'category': 'Jeans', 'id': 12}]>
    cats={item['category'] for item in catProds}
    #thus cats is a list of all categories
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}
    # thus (1,2) means range goes only to 1 from 1
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')
    #to get all products displayed
    # products=Product.objects.all()
    # params={'product':products}
    # return render(request,'shop/about2.html',params)
    # return HttpResponse("We are at about")
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def productview(request,myid):
    #Fetch product using the id
    product=Product.objects.filter(id=myid)
    #print(product)
    return render(request,'shop/prodView.html',{'product':product[0]})

def search(request):
    return render(request,'shop/search.html')

def checkout(request):
        if request.method=='POST':
            items_json=request.POST.get('itemsJson','')
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            address=request.POST.get('address1','')+ " " + request.POST.get('address2','')
            city=request.POST.get('city','')
            state=request.POST.get('state','')
            zip_code=request.POST.get('zip_code','')
            phone=request.POST.get('phone','')
            order=Orders(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
            order.save()
            thank = True;
            id=order.order_id;
            return render(request,'shop/checkout.html',{'thank':thank,'id':id});
        return render(request,'shop/checkout.html')
