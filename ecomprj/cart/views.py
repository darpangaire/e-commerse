from django.shortcuts import render,get_object_or_404
from .cart import Cart
from core.models import Product
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def cart_summary(request):
  #Get the cart
  cart = Cart(request)
  cart_products = cart.get_prods()
  quantities = cart.get_quants()
  totals = cart.cart_total()
  return render(request,"cart_summary.html",{"cart_products":cart_products,"quantities":quantities,"totals":totals}) 

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        try:
            # Retrieve and validate POST data
            product_id = request.POST.get('product_id')
            product_qty = request.POST.get('product_qty')

            if not product_id or not product_qty:
                raise ValueError("Missing product ID or quantity")

            product_id = int(product_id)
            product_qty = int(product_qty)

            # Ensure the product exists in the database
            product = get_object_or_404(Product, id=product_id)

            # Add product to cart
            cart.add(product=product, quantity=product_qty)

            # Get total cart quantity
            cart_quantity = cart.__len__()
            messages.success(request,("product is added in your cart..."))
            return JsonResponse({'qty': cart_quantity})

        except Exception as e:
            print(f"Error in cart_add: {e}")  # Debugging: Log the error
            return JsonResponse({'error': 'An error occurred. Please try again.'}, status=400)



def cart_delete(request):
  cart = Cart(request)
  
  if request.POST.get('action') == 'post':
      try:
              # Retrieve and validate POST data
        product_id = request.POST.get('product_id')
        #call delete Function in Cart
        cart.delete(product = product_id)
        
        response = JsonResponse({'product':product_id})
        messages.success(request,("Items has been deleted..."))       
        return response
        
      
      except:
        pass

def cart_update(request):
  cart = Cart(request)
  
  if request.POST.get('action') == 'post':
      try:
            # Retrieve and validate POST data
          product_id = request.POST.get('product_id')
          product_qty = request.POST.get('product_qty')
          
          cart.update(product = product_id, quantity = product_qty)
          response = JsonResponse({'qty':product_qty})
          messages.success(request,("Your cart has been updated..."))
          return response
          
      except:
        pass
      
      
  

