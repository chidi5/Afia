from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order


# Create your views here.
def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    amount = order.get_total_cost()
    email = order.user.email
    firstname = order.user.first_name,
    lastname = order.user.last_name,

    return render(request, 'payment/process.html',
                  {'order': order, 'amount': amount, 'email': email, 'firstname': firstname, 'lastname': lastname})


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')


'''

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = rave.Card.charge({
            "cardno": "5438898014560229",
            "cvv": "890",
            "expirymonth": "09",
            "expiryyear": "19",
            "amount": '{:.2f}'.format(order.get_total_cost()),
            "email": order.user.email,
            "phonenumber": "0902620185",
            "firstname": order.user.first_name,
            "lastname": order.user.last_name,
        })
        if result["validationRequired"]:
            rave.Card.validate(result["flwRef"], "")

        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.rave_id = result["txRef"]
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')

    else:
        # generate	token
        client_token = rave.Card.validate("flwRef", "")
    '''
