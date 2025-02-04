from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Send email notification
            send_mail(
                subject=f"New Contact Form Submission: {contact_message.subject}",
                message=f"Message from {contact_message.name} ({contact_message.email}):\n\n{contact_message.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['your-website-email@example.com'],  # Change to your website's email
                fail_silently=False,  # If set to True, it will suppress errors (for debugging, keep it False)
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
