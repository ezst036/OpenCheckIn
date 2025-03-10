from . cart import ShoppingCart

def cart(request):
    return{'cart':ShoppingCart(request)}