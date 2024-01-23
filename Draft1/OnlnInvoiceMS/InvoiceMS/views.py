from django.shortcuts import redirect, render

# Create your views here.

from .models import Client, Item, Salesman, Order, Invoice, InvoiceItem, Payment, User

def home(request):
    return render (request, 'InvoiceMS/home.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'InvoiceMS/client_list.html', {'clients': clients})

def clients_insert(request):
    ClientUserID = request.POST.get('ClientUserID')
    ClientName = request.POST.get('ClientName')
    ClientEmail = request.POST.get('ClientEmail')
    ClientPhone = request.POST.get('ClientPhone')
    ClientAddress = request.POST.get('ClientAddress')

    client = Client()

    client.ClientUserID = ClientUserID
    client.ClientName = ClientName
    client.ClientEmail = ClientEmail
    client.ClientPhone = ClientPhone
    client.ClientAddress = ClientAddress
    client.save()
    return redirect ('item_list')

def insertItem(request):
    return render(request, 'InvoiceMS/item_insert.html')

def item_insert(request):
    ItemName = request.POST.get('ItemName')
    ItemBrand = request.POST.get('ItemBrand')
    ItemDescription = request.POST.get('ItemDescription')
    ItemUnitPrice = request.POST.get('ItemUnitPrice')
    ItemQuantity_in_stock = request.POST.get('ItemQuantity_in_stock')

    item = Item()

    item.ItemName = ItemName
    item.ItemBrand = ItemBrand
    item.ItemDescription = ItemDescription
    item.ItemUnitPrice = ItemUnitPrice
    item.ItemQuantity_in_stock = ItemQuantity_in_stock
    item.save()
    return redirect ('item_list')

def item_list(request):
    # current_client = Client.objects.all()'CrntClnt': current_client
    items = Item.objects.all()
    itemListDic = {'items': items} 
    return render(request, 'InvoiceMS/item_list.html', itemListDic)

def salesman_list(request):
    salesmen = Salesman.objects.all()
    return render(request, 'InvoiceMS/salesman_list.html', {'salesmen': salesmen})

def order_list(request):
    # id = request.POST.get('clID')
    # current_client = Client.objects.get(id = id)
    # items = Item.objects.all()
    # orders = Order.objects.all()
    # orderDic = {'items': items, 'CrntClnt': current_client, 'orders': orders} 
    # return render(request, 'InvoiceMS/order_list.html', orderDic)

    # client_id = request.POST.get('ClientID') 'CrntClnt': current_client, 
    # current_client = Client.objects.filter(ClientID=client_id).first()  # Use filter instead of get
    items = Item.objects.all()
    # orders = Order.objects.all()
    order_dic = {'items': items,'orders': orders} 
    return render(request, 'InvoiceMS/order_list.html', order_dic)

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'InvoiceMS/invoice_list.html', {'invoices': invoices})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'InvoiceMS/payment_list.html', {'payments': payments})

def user_list(request):
    users = User.objects.all()
    return render(request, 'InvoiceMS/user_list.html', {'users': users})

