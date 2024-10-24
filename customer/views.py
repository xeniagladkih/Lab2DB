import sys
import os

from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib import messages

import datetime
import decimal

sqlite_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(sqlite_path)

from sqlite import *


def index(request):
    return render(request, 'customer/index.html')


def query_first(request):
    if request.method == 'POST':
        M = str(request.POST.get('category'))
        N = int(request.POST.get('number'))

        data = first_query(M, N)

        customers = Customer.objects.filter(id__in=[row[0] for row in data])

        file_path = 'query_results.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('---------------------------------------------------------------------------------------------------------------\n')
            file.write('Result of Query 1\n')
            file.write('Description: Знайти клієнтів, які замовили не менше @X елементів меню з категорії @Y.\n')
            file.write('Date and Time: {}\n\n'.format(datetime.datetime.now()))

            file.write('Query Parameters:\n')
            file.write('Category: {}\n'.format(M))
            file.write('Number: {}\n\n'.format(N))

            file.write('Obtained Customers:\n')
            for customer in customers:
                file.write('{} {}\n'.format(customer.pk, customer.name))

        context={'customers': customers}
        return render(request, 'customer/query1.html', context)
    
    context={}
    return render(request, 'customer/query1.html', context)


def query_second(request):
    if request.method == 'POST':
        N = str(request.POST.get('city'))

        data = second_query(N)

        orders = Order.objects.filter(id__in=[row[0] for row in data])

        file_path = 'query_results.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('---------------------------------------------------------------------------------------------------------------\n')
            file.write('Result of Query 2\n')
            file.write('Description: Знайти замовлення, які прямували до міста @X та були доставлені.\n')
            file.write('Date and Time: {}\n\n'.format(datetime.datetime.now()))

            file.write('Query Parameters:\n')
            file.write('City: {}\n'.format(N))

            file.write('Obtained Orders:\n')
            for order in orders:
                file.write('{}\n'.format(order.pk))

        context={'orders': orders}
        return render(request, 'customer/query2.html', context)
    
    context={}
    return render(request, 'customer/query2.html', context)


def query_third(request):
    if request.method == 'POST':
        N = int(request.POST.get('number'))

        data = third_query(N)

        customers = Customer.objects.filter(id__in=[row[0] for row in data])

        file_path = 'query_results.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('---------------------------------------------------------------------------------------------------------------\n')
            file.write('Result of Query 3\n')
            file.write('Description: Знайти клієнтів, які зробили принаймні @X замовлень.\n')
            file.write('Date and Time: {}\n\n'.format(datetime.datetime.now()))

            file.write('Query Parameters:\n')
            file.write('Number: {}\n\n'.format(N))

            file.write('Obtained Customers:\n')
            for customer in customers:
                file.write('{} {}\n'.format(customer.pk, customer.name))

        context={'customers': customers}
        return render(request, 'customer/query3.html', context)
    
    context={}
    return render(request, 'customer/query3.html', context)


def query_fourth(request):
    if request.method == 'POST':
        N = str(request.POST.get('email'))

        data = fourth_query(N)

        menu_items = MenuItem.objects.filter(id__in=[row[0] for row in data])
        counts = [row[2] for row in data]

        file_path = 'query_results.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('---------------------------------------------------------------------------------------------------------------\n')
            file.write('Result of Query 4\n')
            file.write('Description: Знайти елементи меню, які були замовлені клієнтом з електронною адресою @X.\n')
            file.write('Date and Time: {}\n\n'.format(datetime.datetime.now()))

            file.write('Query Parameters:\n')
            file.write('Email: {}\n\n'.format(N))

            file.write('Obtained Menu Items:\n')
            for menu_item in menu_items:
                file.write('{}\n'.format(menu_item.name))

        context={'menu_items': menu_items, 'counts': counts}
        return render(request, 'customer/query4.html', context)
    
    context={}
    return render(request, 'customer/query4.html', context)


def query_fifth(request):
    if request.method == 'POST':
        N = str(request.POST.get('category'))

        data = fifth_query(N)

        menu_items = MenuItem.objects.filter(id__in=[row[0] for row in data])

        file_path = 'query_results.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('---------------------------------------------------------------------------------------------------------------\n')
            file.write('Result of Query 5\n')
            file.write('Description: Знайти елементи меню з категорії з назвою @X.\n')
            file.write('Date and Time: {}\n\n'.format(datetime.datetime.now()))

            file.write('Query Parameters:\n')
            file.write('Category: {}\n\n'.format(N))

            file.write('Obtained Menu Items:\n')
            for menu_item in menu_items:
                file.write('{}\n'.format(menu_item.name))

        context={'menu_items': menu_items}
        return render(request, 'customer/query5.html', context)
    
    context={}
    return render(request, 'customer/query5.html', context)


def query_sixth(request):
    if request.method == 'POST':
        N = str(request.POST.get('name'))

        data = sixth_query(N)

        menu_items = MenuItem.objects.filter(id__in=[row[0] for row in data])

        file_path = 'query_results.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('---------------------------------------------------------------------------------------------------------------\n')
            file.write('Result of Query 6\n')
            file.write('Description: Знайти елементи меню, що були замовлені принаймні всіма клієнтами, які замовили елемент меню з назвою @X.\n')
            file.write('Date and Time: {}\n\n'.format(datetime.datetime.now()))

            file.write('Query Parameters:\n')
            file.write('Name: {}\n\n'.format(N))

            file.write('Obtained Menu Items:\n')
            for menu_item in menu_items:
                file.write('{}\n'.format(menu_item.name))

        context={'menu_items': menu_items}
        return render(request, 'customer/query6.html', context)
    
    context={}
    return render(request, 'customer/query6.html', context)


def query_seventh(request):
    if request.method == 'POST':
        N = str(request.POST.get('name'))

        data = seventh_query(N)

        menu_items = MenuItem.objects.filter(id__in=[row[0] for row in data])

        file_path = 'query_results.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('---------------------------------------------------------------------------------------------------------------\n')
            file.write('Result of Query 7\n')
            file.write('Description: Знайти елементи меню, що були в тих і тільки тих замовленнях, в яких був елемент меню з назвою @X.\n')
            file.write('Date and Time: {}\n\n'.format(datetime.datetime.now()))

            file.write('Query Parameters:\n')
            file.write('Name: {}\n\n'.format(N))

            file.write('Obtained Menu Items:\n')
            for menu_item in menu_items:
                file.write('{}\n'.format(menu_item.name))

        context={'menu_items': menu_items}
        return render(request, 'customer/query7.html', context)
    
    context={}
    return render(request, 'customer/query7.html', context)


def query_eighth(request):
    if request.method == 'POST':
        N = str(request.POST.get('email'))

        data = eighth_query(N)

        customers = Customer.objects.filter(id__in=[row[0] for row in data])

        file_path = 'query_results.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('---------------------------------------------------------------------------------------------------------------\n')
            file.write('Result of Query 8\n')
            file.write('Description: Знайти клієнтів, які замовляли всі елементи меню, що і клієнт з електронною адресою @X.\n')
            file.write('Date and Time: {}\n\n'.format(datetime.datetime.now()))

            file.write('Query Parameters:\n')
            file.write('Number: {}\n\n'.format(N))

            file.write('Obtained Customers:\n')
            for customer in customers:
                file.write('{} {}\n'.format(customer.pk, customer.name))

        context={'customers': customers}
        return render(request, 'customer/query8.html', context)
    
    context={}
    return render(request, 'customer/query8.html', context)


def menu_item(request):
    menu_items = MenuItem.objects.all()
    context = {'menu_items': menu_items}
    return render(request, 'customer/menu_item/menu_item.html', context)


def category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'customer/category/category.html', context)


def customer(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer/customer/customer.html', context)


def order(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'customer/order/order.html', context)


def order_item(request):
    order_items = OrderModel.objects.all()
    context = {'order_items': order_items}
    return render(request, 'customer/order_item/order_item.html', context)


def shipping_address(request):
    shipping_addresses = ShippingAddress.objects.all()
    context = {'shipping_addresses': shipping_addresses}
    return render(request, 'customer/shipping_address/shipping_address.html', context)


def view_menu_item(request, id):
    menu_item = MenuItem.objects.get(pk=id)
    return HttpResponseRedirect(reverse('menu-item'))


def view_category(request, id):
    category = Category.objects.get(pk=id)
    return HttpResponseRedirect(reverse('category'))


def view_customer(request, id):
    customer = Customer.objects.get(pk=id)
    return HttpResponseRedirect(reverse('customer'))


def view_order(request, id):
    order = Order.objects.get(pk=id)
    return HttpResponseRedirect(reverse('order'))


def view_order_item(request, id):
    order_item = OrderModel.objects.get(pk=id)
    return HttpResponseRedirect(reverse('order-item'))


def view_shipping_address(request, id):
    shipping_address = ShippingAddress.objects.get(pk=id)
    return HttpResponseRedirect(reverse('shipping-address'))


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_description = form.cleaned_data['description']
            new_image = form.cleaned_data['image']
            new_price = form.cleaned_data['price']
            new_category = form.cleaned_data['category']

            if new_name in list(MenuItem.objects.values_list('name', flat=True).distinct()):
                messages.warning(request, "Menu Item with this name already exists!")
            elif new_price <=0:
                messages.error(request, "Price has to be positive!")
            elif type(new_price) != decimal and new_price % 1 != 0:
                messages.error(request, "Price has to be integer!")
            else:
                new_menu_item = MenuItem(
                    name=new_name,
                    description=new_description,
                    image=new_image,
                    price=new_price,
                    category=Category.objects.get(name=new_category)
                )
                new_menu_item.save()

                context = {
                    'form': MenuItemForm(),
                    'success': True,
                }

                return render(request, 'customer/menu_item/menu_item_add.html', context)
        else:
            print('Invalid')
    else:
        form = MenuItemForm()
    return render(request, 'customer/menu_item/menu_item_add.html', {'form': MenuItemForm()})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']

            if new_name in list(Category.objects.values_list('name', flat=True).distinct()):
                messages.warning(request, "Category with this name already exists!")
            else:
                new_category = Category(
                    name=new_name
                )
                new_category.save()

                context = {
                    'form': CategoryForm(),
                    'success': True,
                }

                return render(request, 'customer/category/category_add.html', context)
        else:
            print('Invalid')
    else:
        form = CategoryForm()
    return render(request, 'customer/category/category_add.html', {'form': CategoryForm()})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_user = form.cleaned_data['user']
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_phone = form.cleaned_data['phone']

            if new_email in list(Customer.objects.values_list('email', flat=True).distinct()):
                messages.warning(request, "Customer with this email already exists!")
            elif new_user and new_email != User.objects.get(username=new_user).email:
                messages.warning(request, "Wrong email for this user!")
            else:
                new_customer = Customer(
                    user = User.objects.get(username=new_user),
                    name=new_name,
                    email=new_email,
                    phone=new_phone
                )
                new_customer.save()

                context = {
                    'form': CustomerForm(),
                    'success': True,
                }

                return render(request, 'customer/customer/customer_add.html', context)
        else:
            print('Invalid')
    else:
        form = CustomerForm()
    return render(request, 'customer/customer/customer_add.html', {'form': CustomerForm()})


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_customer = form.cleaned_data['customer']
            new_complete = form.cleaned_data['complete']
            new_transaction_id = form.cleaned_data['transaction_id']
            new_is_shipped = form.cleaned_data['is_shipped']

            new_order = Order(
                customer=Customer.objects.get(email=new_customer),
                complete=new_complete,
                transaction_id=new_transaction_id,
                is_shipped=new_is_shipped
            )
            new_order.save()

            context = {
                'form': OrderForm(),
                'success': True,
            }

            return render(request, 'customer/order/order_add.html', context)
        else:
            print('Invalid')
    else:
        form = OrderForm()
    return render(request, 'customer/order/order_add.html', {'form': OrderForm()})


def add_order_item(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            new_menu_item = form.cleaned_data['menu_item']
            new_order = form.cleaned_data['order']
            new_quantity = form.cleaned_data['quantity']

            new_order_item = OrderModel(
                menu_item=MenuItem.objects.get(name=new_menu_item),
                order=Order.objects.get(pk=new_order.id),
                quantity=new_quantity
            )
            new_order_item.save()

            context = {
                'form': OrderItemForm(),
                'success': True,
            }

            return render(request, 'customer/order_item/order_item_add.html', context)
        else:
            print('Invalid')
    else:
        form = OrderItemForm()
    return render(request, 'customer/order_item/order_item_add.html', {'form': OrderItemForm()})


def add_shipping_address(request):
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            new_customer = form.cleaned_data['customer']
            new_order = form.cleaned_data['order']
            new_address = form.cleaned_data['address']
            new_city = form.cleaned_data['city']

            new_shipping_address= ShippingAddress(
                customer=Customer.objects.get(email=new_customer),
                order=Order.objects.get(pk=new_order.id),
                address = new_address,
                city=new_city
            )
            new_shipping_address.save()

            context = {
                'form': ShippingAddressForm(),
                'success': True,
            }

            return render(request, 'customer/shipping_address/shipping_address_add.html', context)
        else:
            print('Invalid')
    else:
        form = ShippingAddressForm()
    return render(request, 'customer/shipping_address/shipping_address_add.html', {'form': ShippingAddressForm()})


def edit_menu_item(request, id):
    if request.method == 'POST':
        menu_item = MenuItem.objects.get(pk=id)
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():

            if form.cleaned_data['price'] <= 0:
                messages.error(request, "Price has to be positive!")
            else:
                form.save()

                context = {
                    'form': form,
                    'success': True,
                }

                return render(request, 'customer/menu_item/menu_item_edit.html', context)   
    else:
        menu_item = MenuItem.objects.get(pk=id)
        form = MenuItemForm(instance=menu_item)
    return render(request, 'customer/menu_item/menu_item_edit.html', {'form': form})


def edit_category(request, id):
    category = Category.objects.get(pk=id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()

            context = {
                'form': form,
                'success': True,
            }

            return render(request, 'customer/category/category_edit.html', context)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'customer/category/category_edit.html', {'form': form})


def edit_customer(request, id):
    if request.method == 'POST':
        customer = Customer.objects.get(pk=id)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()

            context = {
                'form': form,
                'success': True,
            }

            return render(request, 'customer/customer/customer_edit.html', context)   
    else:
        customer = Customer.objects.get(pk=id)
        form = CustomerForm(instance=customer)
    return render(request, 'customer/customer/customer_edit.html', {'form': form})


def edit_order(request, id):
    if request.method == 'POST':
        order = Order.objects.get(pk=id)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()

            context = {
                'form': form,
                'success': True,
            }

            return render(request, 'customer/order/order_edit.html', context)   
    else:
        order = Order.objects.get(pk=id)
        form = OrderForm(instance=order)
    return render(request, 'customer/order/order_edit.html', {'form': form})


def edit_order_item(request, id):
    if request.method == 'POST':
        order_item = OrderModel.objects.get(pk=id)
        form = OrderItemForm(request.POST, instance=order_item)
        if form.is_valid():
            form.save()

            context = {
                'form': form,
                'success': True,
            }

            return render(request, 'customer/order_item/order_item_edit.html', context)   
    else:
        order_item = OrderModel.objects.get(pk=id)
        form = OrderItemForm(instance=order_item)
    return render(request, 'customer/order_item/order_item_edit.html', {'form': form})


def edit_shipping_address(request, id):
    if request.method == 'POST':
        shipping_address = ShippingAddress.objects.get(pk=id)
        form = ShippingAddressForm(request.POST, instance=shipping_address)
        if form.is_valid():
            form.save()

            context = {
                'form': form,
                'success': True,
            }

            return render(request, 'customer/shipping_address/shipping_address_edit.html', context)   
    else:
        shipping_address = ShippingAddress.objects.get(pk=id)
        form = ShippingAddressForm(instance=shipping_address)
    return render(request, 'customer/shipping_address/shipping_address_edit.html', {'form': form})


def delete_menu_item(request, id):
    if request.method=="POST":
        menu_item = MenuItem.objects.get(pk=id)
        menu_item.delete()
    return HttpResponseRedirect(reverse('menu-item'))


def delete_category(request, id):
    if request.method=="POST":
        category = Category.objects.get(pk=id)
        category.delete()
    return HttpResponseRedirect(reverse('category'))


def delete_customer(request, id):
    if request.method=="POST":
        customer = Customer.objects.get(pk=id)
        customer.delete()
    return HttpResponseRedirect(reverse('customer'))


def delete_order(request, id):
    if request.method=="POST":
        order = Order.objects.get(pk=id)
        order.delete()
    return HttpResponseRedirect(reverse('order'))


def delete_order_item(request, id):
    if request.method=="POST":
        order_item = OrderModel.objects.get(pk=id)
        order_item.delete()
    return HttpResponseRedirect(reverse('order-item'))


def delete_shipping_address(request, id):
    if request.method=="POST":
        shipping_address = ShippingAddress.objects.get(pk=id)
        shipping_address.delete()
    return HttpResponseRedirect(reverse('shipping-address'))