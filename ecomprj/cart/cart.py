from core.models import Product,Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request

        # Attempt to retrieve the cart, or initialize a new one if it doesn't exist
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['session_key'] = {}

        # Assign the cart to the instance
        self.cart = cart
        self.session.modified = True
        
    def db_add(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)

        if product_id in self.cart:
            self.cart[product_id] = self.cart.get(product_id,0) + 1
        else:
            self.cart[product_id] = product_qty

        self.session.modified = True
        
        # Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            # convert {'3':1,'2':4} to {"3":1,"2":4}
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # save carty to the Profile Model
            current_user.update(old_cart=str(carty))
        

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)

        if product_id in self.cart:
            self.cart[product_id] = self.cart.get(product_id,0) + 1
        else:
            self.cart[product_id] = product_qty

        self.session.modified = True
        
        # Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            # convert {'3':1,'2':4} to {"3":1,"2":4}
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # save carty to the Profile Model
            current_user.update(old_cart=str(carty))
            
            

    def __len__(self):
        return sum(self.cart.values())

    def get_prods(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_quants(self):
        return self.cart
    
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
        #get Cart
        ourcart = self.cart
        #update Dictionary/cart
        ourcart[product_id] = product_qty
        self.session.modified = True
        
        
        
        # Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            # convert {'3':1,'2':4} to {"3":1,"2":4}
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # save carty to the Profile Model
            current_user.update(old_cart=str(carty))
            
        thing = self.cart
  
        return thing
    
    def delete(self,product):
        product_id = str(product)
        #Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True
        
        # Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            # convert {'3':1,'2':4} to {"3":1,"2":4}
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # save carty to the Profile Model
            current_user.update(old_cart=str(carty))
  
        

    def cart_total(self):
        # Get product IDS
        product_ids = self.cart.keys()
        # lookup those keys in our products database model
        products = Product.objects.filter(id__in = product_ids)
        
        # Get quantities
        quantities = self.cart
        # start counting at 0
        total = 0
        for key,value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                        
                    else:
                        total = total + (product.price * value)
        return total
        

  
    
     
    
    