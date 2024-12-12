from django.core.mail import send_mail
from django.conf import settings

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
