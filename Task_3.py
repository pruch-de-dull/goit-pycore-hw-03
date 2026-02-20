import re


def normalize_phone(phone_number: str) -> str:
    phone_number_cleaned = re.sub(r'[^+\d]', '', phone_number.strip())
    
    if phone_number_cleaned.startswith('+38'):
        new_phone = phone_number_cleaned
    elif phone_number_cleaned.startswith('+'):
        new_phone = phone_number_cleaned
    elif phone_number_cleaned.startswith('380'):
        new_phone = f'+{phone_number_cleaned}' 
    else:
        new_phone = f"+38{phone_number_cleaned}"
        
    return new_phone
    

if __name__ == "__main__":
    f = normalize_phone('    +38(050)123-32-34')
    print(f)
