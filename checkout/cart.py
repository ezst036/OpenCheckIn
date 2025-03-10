from django.conf import settings
from . models import Product
from decimal import Decimal

class ShoppingCart(object):
    def __init__(self, request):
        self.session=request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart=cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['display_price']=item['price'] / 100
            item['total_price']=(item['price'] * item['quantity']) / 100
            yield item
        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        finalval=sum(Decimal((item['price']) * item['quantity']) for item in self.cart.values())

        total=0
        for cartitem in self.cart:
            price=self.cart[str(cartitem)]['price']
            qty=self.cart[str(cartitem)]['quantity']
            total+=price * qty

        finalval=round(Decimal(total / 100), 2)

        return finalval
    
    def clear(self):
        # empty cart
        del self.session[settings.CART_SESSION_ID]
        self.save()
    
    def add(self, product, quantity=1, update_quantity=False):
        productid = str(product.id)
        if productid not in self.cart:
            self.cart[productid]={'quantity':0, 'price':product.price}
        
        if update_quantity:
            self.cart[productid]['quantity'] = quantity
        else:
            self.cart[productid]['quantity'] += quantity
        self.save()
    
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
    def remove(self, product):
        productid = str(product.id)
        if productid in self.cart:
            del self.cart[productid]
            self.save()