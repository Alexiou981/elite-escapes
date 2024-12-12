from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event['data']['object']  # Extract the object
        print("Payment Intent:", intent)  # Debug log

        # Check the structure
        customer_email = intent.get('charges', {}).get('data', [{}])[0].get('billing_details', {}).get('email', None)
        print("Customer Email:", customer_email)

        # Add further logic here
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
    def send_booking_confirmation_email(user_email, package_name, total_price):
        subject = "Your Elite Escapes Booking Confirmation"
        message = (
            f"Dear Customer,\n\n"
            f"Thank you for booking with Elite Escapes!\n\n"
            f"Package: {package_name}\n"
            f"Total Price: ${total_price}\n\n"
            f"We hope you have an amazing experience!\n"
            f"Best regards,\nThe Elite Escapes Team"
        )
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]

        send_mail(subject, message, email_from, recipient_list)