from django.shortcuts import redirect
from django.template.response import TemplateResponse

from saleor.checkout.forms import CartShippingMethodForm
from saleor.shipping.models import ShippingMethod
from ..utils import (
    get_cart_data_for_checkout, get_taxes_for_cart,
    update_shipping_address_in_anonymous_cart, update_shipping_address_in_cart, is_valid_shipping_method)


def anonymous_user_shipping_address_view(request, cart):
    """Display the shipping step for a user who is not logged in."""
    user_form, address_form, updated = (
        update_shipping_address_in_anonymous_cart(
            cart, request.POST or None, request.country))

    if updated:
        return redirect('checkout:shipping-method')

    taxes = get_taxes_for_cart(cart, request.taxes)
    ctx = get_cart_data_for_checkout(cart, request.discounts, taxes)
    ctx.update({
        'address_form': address_form,
        'user_form': user_form})
    return TemplateResponse(request, 'checkout/shipping_address.html', ctx)


def user_shipping_address_view(request, cart):
    """Display the shipping step for a logged in user.

    In addition to entering a new address the user has an option of selecting
    one of the existing entries from their address book.
    """
    cart.email = request.user.email
    cart.save(update_fields=['email'])
    user_addresses = cart.user.addresses.all()

    addresses_form, address_form, updated, country_code, initial_address = update_shipping_address_in_cart(
        cart, user_addresses, request.POST or None, request.country, request.POST.get('triggered_by_country', False))
    print(country_code)
    print(initial_address)

    discounts = request.discounts
    taxes = get_taxes_for_cart(cart, request.taxes)
    is_valid_shipping_method(cart, request.taxes, discounts)

    form = CartShippingMethodForm(
        request.POST or None, discounts=discounts, taxes=taxes, instance=cart,
        initial={'shipping_method': cart.shipping_method, 'selected_country': country_code})

    if form.is_valid() and updated:
        form.save()
        return redirect('checkout:summary')
    else:
        is_shipping_method_available = ShippingMethod.objects.filter(
            shipping_zone__countries__contains=country_code).exists()

        if not is_shipping_method_available:
            try:
                address_form.add_error('country', 'Shipping method for selected country is not available.')
            except Exception as e:
                print(e)

    ctx = get_cart_data_for_checkout(cart, discounts, taxes)
    ctx.update({
        'additional_addresses': user_addresses,
        'address_form': address_form,
        'user_form': addresses_form,
        'shipping_method_form': form,
        'initialAddress': initial_address,
        'shippingAddress': True})
    return TemplateResponse(request, 'checkout/shipping_address.html', ctx)
