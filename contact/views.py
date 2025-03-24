from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Custom email with sender's name
            email_subject = (
                f"New Contact Form Submission: {contact_message.subject}"
            )
            email_body = f"""
            You have received a new contact form submission:

            Name: {contact_message.name}
            Email: {contact_message.email}
            Subject: {contact_message.subject}
-
            Message:
            {contact_message.message}
            """

            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=(
                    f"{contact_message.name} via My Website "
                    f"<{settings.EMAIL_HOST_USER}>"
                ),  # Custom sender name
                to=['escapeselite79@gmail.com'],
                reply_to=[
                    contact_message.email
                ],  # Ensures replies go to the user
            )
            email.send(fail_silently=False)

            messages.success(
                request, "Your message has been sent successfully!"
            )
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
