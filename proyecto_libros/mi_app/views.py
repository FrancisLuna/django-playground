from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Product, Order, OrderItem
from .forms import CustomerForm, ExistingCustomerForm, OrderItemForm, OrderQueryForm

def inicio(request):
    # return render(request, "Hola")
    return render(request, "mi_app/index.html")

def libro_list(request):
    libros = Product.objects.all()
    return render(request, "mi_app/libro_list.html", {'libros': libros})





def usuario_list(request):
    return render(request, "mi_app/usuario_list.html")

def carrito_list(request):
    return render(request, "mi_app/carrito_list.html")


########################################################################################
def create_order(request):
    if request.method == 'POST':
        existing_customer_form = ExistingCustomerForm(request.POST)
        new_customer_form = CustomerForm(request.POST)
        order_items_data = zip(request.POST.getlist('product'), request.POST.getlist('quantity'))

        customer = None
        if existing_customer_form.is_valid() and existing_customer_form.cleaned_data['customer']:
            customer = existing_customer_form.cleaned_data['customer']
        elif not existing_customer_form.cleaned_data['customer'] and new_customer_form.is_valid():
            customer = new_customer_form.save()
        
        if customer:
            order = Order.objects.create(customer=customer)
            for product_id, quantity in order_items_data:
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)
            return redirect('order_confirmation', order_id=order.id)
        else:
            return render(request, 'mi_app/create_order.html', {
                'existing_customer_form': existing_customer_form,
                'new_customer_form': new_customer_form,
                'order_item_forms': [OrderItemForm()] * len(request.POST.getlist('product')),
                'products': Product.objects.all(),
                'error': "Por favor, seleccione un cliente existente o complete los campos para crear uno nuevo.",
            })

    else:
        existing_customer_form = ExistingCustomerForm()
        new_customer_form = CustomerForm()
        order_item_forms = [OrderItemForm()]

    products = Product.objects.all()

    return render(request, 'mi_app/create_order.html', {
        'existing_customer_form': existing_customer_form,
        'new_customer_form': new_customer_form,
        'order_item_forms': order_item_forms,
        'products': products,
    })


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'mi_app/order_confirmation.html', {
        'order': order,
        'order_items': order_items,
    })

def query_order(request):
    if request.method == 'POST':
        form = OrderQueryForm(request.POST)
        if form.is_valid():
            order_number = form.cleaned_data['order_number']
            try:
                order = get_object_or_404(Order, id=order_number)
                order_items = OrderItem.objects.filter(order=order)
                if order_items.exists():
                    return render(request, 'mi_app/order_detail.html', {
                        'order': order,
                        'order_items': order_items,
                    })
                else:
                    return render(request, 'mi_app/query_order.html', {
                        'form': form,
                        'error': "No se encontró la orden con el número ingresado.",
                    })
            except:
                return render(request, 'mi_app/query_order.html', {
                    'form': form,
                    'error': "No se encontró el pedido.",
                })
    else:
        form = OrderQueryForm()

    return render(request, 'mi_app/query_order.html', {'form': form})
