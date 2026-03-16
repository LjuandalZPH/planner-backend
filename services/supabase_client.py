#/ Supabase SDK Client Initialization
#/This module initializes the official Supabase Python SDK client

#Purpose:
#- Handles Authentication (Sign-up, Login, Password Recovery).
#- Manages direct API interactions with Supabase services via HTTPS (Port 443).
#- Provides a centralized 'supabase' instance to be used across the application services.

#Security Note:
#- Uses the 'SUPABASE_ANON_KEY' for client-side/publicly safe operations.
#- Environment variables are loaded from the local .env file using 'python-dotenv'.

  

import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY") 

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Faltan SUPABASE_URL o SUPABASE_ANON_KEY en el entorno")


supabase = create_client(SUPABASE_URL, SUPABASE_KEY)