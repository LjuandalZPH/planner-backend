"""
Authentication Views Module
---------------------------
This module provides API endpoints for user identity management using the Supabase Auth SDK.
Instead of using Django's internal authentication system, these views delegate user 
registration and credential verification to Supabase via its Python SDK.

Workflow:
1. Receive user credentials via POST request.
2. Forward data to Supabase Auth service.
3. Return the Supabase session (including JWT) or error message back to the client.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.supabase_client import supabase


@api_view(["POST"])
def register(request):
    email = request.data.get("email")
    password = request.data.get("password")

    res = supabase.auth.sign_up({
        "email": email,
        "password": password
    })

    return Response(res)


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    res = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

    return Response(res)