from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from museapi.models import Artist, Medium
import json


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            req_body = json.loads(request.body.decode("utf-8"))
            username = req_body.get("username")
            password = req_body.get("password")

            if username and password:
                user = authenticate(username=username, password=password)
                if user:
                    token, _ = Token.objects.get_or_create(user=user)
                    return JsonResponse({"token": token.key, "id": user.id})
                else:
                    return JsonResponse({"error": "Invalid credentials"}, status=400)
            else:
                return JsonResponse(
                    {"error": "Username and password are required"}, status=400
                )
        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON format in request body"}, status=400
            )
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            req_body = json.loads(request.body.decode("utf-8"))
            required_fields = [
                "username",
                "password",
                "email",
                "first_name",
                "last_name",
                "phone_number",
                "address",
                "preferred_medium",  # Added preferred_medium to required fields
            ]
            for field in required_fields:
                if field not in req_body:
                    return JsonResponse(
                        {"error": f"Field '{field}' is required"}, status=400
                    )

            new_user = User.objects.create_user(
                username=req_body["username"],
                email=req_body["email"],
                password=req_body["password"],
                first_name=req_body["first_name"],
                last_name=req_body["last_name"],
            )

            # Retrieve the medium instance based on the preferred_medium field
            preferred_medium_id = req_body["preferred_medium"]
            medium_instance = Medium.objects.get(pk=preferred_medium_id)

            artist = Artist.objects.create(
                bio=req_body["bio"],
                preferred_medium=medium_instance,
                user=new_user,
            )

            token, _ = Token.objects.get_or_create(user=new_user)
            return JsonResponse({"token": token.key, "id": new_user.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON format in request body"}, status=400
            )
        except Medium.DoesNotExist:
            return JsonResponse(
                {"error": "Preferred medium does not exist"}, status=400
            )
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
