import random
class ShopFacade:
    def __init__(self):
        self.ordering_system = OrderingSystem()
        self.payment_gateway = PaymentGateway()
        self.delivery_service = DeliveryService()

    def place_order(self, customer_info, order_info):
        order_id = self.ordering_system.create_order(customer_info, order_info)
        payment_status = self.payment_gateway.process_payment(order_id)
        if payment_status == 'success':
            delivery_info = self.delivery_service.schedule_delivery(order_id)
            return f'Your order has been placed successfully! Your order ID is {order_id}. ' \
                   f'Your delivery will arrive on {delivery_info["delivery_date"]} ' \
                   f'at {delivery_info["delivery_time"]}.'
        else:
            return 'Payment processing failed. Please try again later.'


import uuid
import datetime


class OrderingSystem:
    def create_order(self, customer_info, order_info):
        # generate order id
        order_id = str(uuid.uuid4())

        # create order record
        order_record = {
            'order_id': order_id,
            'customer_name': customer_info['name'],
            'customer_phone': customer_info['phone'],
            'order_items': order_info['items'],
            'total_amount': order_info['total']
        }

        # save order record to database
        # ...

        return order_id


class PaymentGateway:
    def process_payment(self, order_id):
        # simulate payment processing
        payment_status = 'success'
        return payment_status


class DeliveryService:
    def schedule_delivery(self, order_id):
        # calculate delivery date and time
        delivery_date = datetime.date.today() + datetime.timedelta(days=2)
        delivery_time = datetime.time(hour=14)

        # create delivery record
        delivery_record = {
            'order_id': order_id,
            'delivery_date': delivery_date,
            'delivery_time': delivery_time
        }

        # save delivery record to database
        # ...

        return delivery_record

