def sum_delivery(delivery):
        total = sum(item.dish.price*item.amount for item in delivery.order.item_set.all())
        return total