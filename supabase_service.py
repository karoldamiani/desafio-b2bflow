import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

def get_contacts():
    response = (
        supabase
        .table("contatos")
        .select("*")
        .limit(3)
        .execute()
    )

    return response.data