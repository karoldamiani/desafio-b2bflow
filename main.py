from supabase_service import get_contacts
from zapi_service import send_message

try:
    contacts = get_contacts()

    for contact in contacts:
        name = contact["nome"]
        phone = contact["telefone"]

        message = (
             f"Olá, {name} tudo bem com você?"
        )

        response = send_message(
            phone, 
            message
        )

        print(f"{name} - Status: {response.status_code}")

except Exception as error:
    print(f"Error: {error}")