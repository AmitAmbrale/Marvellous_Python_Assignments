import email_validator

def CheckEmail(Email):

    try:
        email_validator.validate_email(Email)
    except Exception:
        print("Invalid email")
        exit()