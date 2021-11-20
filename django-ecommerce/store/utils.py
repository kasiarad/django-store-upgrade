import json
from .models import *


def cookieCart(request):
	# Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('CART:', cart)

	items = []
	order = {'all_cart_value': 0, 'all_cart_quantity': 0, 'shipping': False}
	cartItems = order['all_cart_quantity']

	for i in cart:
		# We use try block to prevent items in cart that may have been removed from causing error
		try:
			cartItems += cart[i]['quantity']

			product = Product.objects.get(id=i)
			total = (product.price * cart[i]['quantity'])

			order['all_cart_value'] += total
			order['all_cart_quantity'] += cart[i]['quantity']

			item = {
				'product': {'id': product.id, 'name': product.name, 'price': product.price,
							'imageURL': product.imageURL}, 'quantity': cart[i]['quantity'],
				'get_total': total,
			}
			items.append(item)

		except:
			pass

	return {'cartItems': cartItems, 'order': order, 'items': items}

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.all_cart_quantity
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	return {'cartItems':cartItems ,'order':order, 'items':items}

def guestOrder(request, data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	order = Order.objects.create(
		complete=False,
	)
	print(items)
	for item in items:
		product = Product.objects.get(id=item['product']['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=(item['quantity'] if item['quantity'] > 0 else -1 * item['quantity']),
			# negative quantity = freebies
		)
	return name, order
