from celery import task
from django.core.mail import send_mail
from .models import Order

@task 
def order_created(order_id):
    """
    Task to send an email notification when an order is sucessfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n You have sucessfully placed an order. \n\nYour order ID is {order.id}'
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent