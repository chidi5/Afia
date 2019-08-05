from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """ Task to	send an	e-mail notification	when an	order is successfully created. """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr.{}'.format(order.id)
    if order.first_name is None:
        message = 'Dear {},\n\nYou have successfully placed an order.\ Your order id is {}.'.format(
            order.user.first_name, order.id)
    else:
        message = 'Dear	{},\n\nYou have successfully placed an order.\ Your order id is {}.'.format(order.first_name,
                                                                                                       order.id)

    mail_sent = send_mail(subject, message, 'admin@Afia.com', [order.user.email])
    return mail_sent
