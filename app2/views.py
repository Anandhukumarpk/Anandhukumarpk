from django.shortcuts import render , redirect , get_object_or_404
from .models import  Order, OrderItem ,Contactus
from django.contrib.contenttypes.models import ContentType

from cart.models import CartItem 
from .forms import ContactForm
from django.views.decorators.csrf  import csrf_protect






# Create your views here.


def orderplace(request):
    # Get the cart items for the current user
    cart_items = CartItem.objects.filter(user=request.user)
    
    # Create a new order
    new_order = Order.objects.create(user=request.user)

    

    # Loop through each cart item and create an OrderItem
    for cart_item in cart_items:
        OrderItem.objects.create(
            order=new_order,
            content_type=cart_item.content_type,
            object_id=cart_item.object_id,
            quantity=cart_item.quantity,
            price=cart_item.product.price  # Save the price at the time of order
        )
    
    # Calculate the total price of the order
    total = sum(item.total_price for item in new_order.items.all())
    new_order.total_price = total
    new_order.save()

   
    return redirect( 'placeorder')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Use correct form name (ContactForm)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect or change as per your logic
    else:
        form = ContactForm() 
   
    return render (request, 'contactus.html', {'form': form})

def orderpage(request):

    
    
    return render (request , 'orders.html' )
    
 

def confirmOrder(request,):
    context = {}
    if request.method == 'POST':
       
        client = razorpay.Client(auth=('rzp_test_kVb2FiWBE8oiA2', 'PgNMROhqrrfn5n64FmGDqAYK'))
        payment = client.order.create({
            'amount': '50000',  # Use the calculated cart total in paise
            'currency': 'INR',
            'payment_capture': '1'
        })

        
    
    return render (request , 'completeOrder.html' )
    
@csrf_protect
def payment(request):
    
    return render (request, 'payment.html')



def cart(request):

     if not request.user.is_authenticated:
        return redirect('login')
     
    
     cart_items = CartItem.objects.filter(user=request.user)
     cart_total = sum(item.total_price for item in cart_items)


     return render(request , 'Cart.html' , {
         'cart_items': cart_items,
        'cart_total': cart_total,
     })


def faq(request):
    return render(request, 'faq.html')

