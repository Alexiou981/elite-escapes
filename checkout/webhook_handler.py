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
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        customer_email = intent['charges']['data'][0]['billing_details']['email']
        metadata = intent.get('metadata', {})
        package_id = metadata.get('package_id')
        total_price = metadata.get('total_price')
        user_id = metadata.get('user_id')

        if package_id and total_price and user_id:
            try:
                package = Package.objects.get(id=package_id)
                user = User.objects.get(id=user_id)
                Booking.objects.create(
                    user=user,
                    package=package,
                    amount=total_price,
                )

                # Send confirmation email
                send_booking_confirmation_email(
                    user_email=customer_email,
                    package_name=package.name,
                    total_price=total_price,
                )
            except (Package.DoesNotExist, User.DoesNotExist) as e:
                return HttpResponse(content=f"Error creating booking: {e}", status=500)

        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)

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