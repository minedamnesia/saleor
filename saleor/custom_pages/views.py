# Create your views here.
from django.template.response import TemplateResponse


def about_us(request):
    return TemplateResponse(request, 'custom_pages/upcoming_events.html', {'message': 'About Us'})


def faq(request):
    return TemplateResponse(request, 'custom_pages/upcoming_events.html', {'message': 'FAQs'})


def policy(request):
    return TemplateResponse(request, 'custom_pages/upcoming_events.html', {'message': 'Privacy Policy'})


def shipping_policy(request):
    return TemplateResponse(request, 'custom_pages/upcoming_events.html', {'message': 'Shipping Policy'})


def tos(request):
    return TemplateResponse(request, 'custom_pages/upcoming_events.html', {'message': 'Terms of Service'})


def upcoming_events(request):
    return TemplateResponse(request, 'custom_pages/upcoming_events.html', {'message': 'Upcoming Events'})
