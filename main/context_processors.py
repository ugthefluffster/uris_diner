from main.models import *

def site_wide_data(request):
    try:
        data = {
        'open_orders_number' : len(Cart.objects.filter(delivery__is_delivered=False)),
        'my_open_orders_number' : len(Delivery.objects.filter(order__user=request.user).filter(is_delivered=False)),
        'my_cart_items_number' : len(User.objects.get(id=request.user.id).cart_set.last().item_set.all())
        }
    except:
        data = {}
    return data