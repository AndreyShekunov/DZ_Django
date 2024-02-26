from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime, timedelta
from .models import Client, Product, Order


# Для клиента
def create_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        new_client = Client(name=name, email=email, phone_number=phone_number, address=address)
        new_client.save()
        return JsonResponse({'message': 'Клиент успешно создан'}, status=201)


def get_all_clients(request):
    clients = Client.objects.all()
    data = [{'name': client.name, 'email': client.email, 'phone_number': client.phone_number, 'address': client.address,
             'registration_date': client.registration_date} for client in clients]
    return JsonResponse(data, safe=False)


def update_client(request, client_id):
    client = Client.objects.get(id=client_id)
    client.name = request.POST.get('name', client.name)
    client.email = request.POST.get('email', client.email)
    client.phone_number = request.POST.get('phone_number', client.phone_number)
    client.address = request.POST.get('address', client.address)
    client.save()
    return JsonResponse({'message': 'Клиент обновлен успешно'}, status=200)


def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return JsonResponse({'message': 'Клиент успешно удален'}, status=204)


# Для продукта
def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        new_product = Product(name=name, description=description, price=price, quantity=quantity)
        new_product.save()
        return JsonResponse({'message': 'Продукт успешно создан'}, status=201)


def get_all_products(request):
    products = Product.objects.all()
    data = [{'name': product.name, 'description': product.description, 'price': str(product.price),
             'quantity': product.quantity, 'added_date': product.added_date} for product in products]
    return JsonResponse(data, safe=False)


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.name = request.POST.get('name', product.name)
    product.description = request.POST.get('description', product.description)
    product.price = request.POST.get('price', product.price)
    product.quantity = request.POST.get('quantity', product.quantity)
    product.save()
    return JsonResponse({'message': 'Продукт успешно обновлен'}, status=200)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return JsonResponse({'message': 'Товар успешно удален'}, status=204)


# Для заказа
def create_order(request):
    if request.method == 'POST':
        client_id = request.POST['client_id']
        products_ids = request.POST.getlist('products_ids')
        total_amount = request.POST['total_amount']
        new_order = Order(client_id=client_id, total_amount=total_amount)
        new_order.save()
        new_order.products.set(products_ids)
        return JsonResponse({'message': 'Заказ успешно создан'}, status=201)


def get_all_orders(request):
    orders = Order.objects.all()
    data = [{'client': order.client.name, 'total_amount': str(order.total_amount), 'order_date': order.order_date} for
            order in orders]
    return JsonResponse(data, safe=False)


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    total_amount = request.POST.get('total_amount', order.total_amount)
    order.total_amount = total_amount
    order.save()
    return JsonResponse({'message': 'Заказ успешно обновлен'}, status=200)


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return JsonResponse({'message': 'Заказ успешно удален'}, status=204)
