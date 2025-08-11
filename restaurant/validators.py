import re

def invalid_phone(phone):
    # 99 99999-9999
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    return not phone or len(phone) != 13 or not re.fullmatch(model, phone)

def invalid_email(email):
    return not email or '@' not in email

def invalid_name(name):
    return not name or len(name) < 3 or not name.replace(" ", "").isalpha()