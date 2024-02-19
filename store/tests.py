from django.test import TestCase


def validate_uz_phone_number(phone_number: str):
    uzb = phone_number.count('+998')

    if uzb == 1:
        print("True")
    elif len(phone_number) != 13:
        print("False")
    else:
        print("False")


validate_uz_phone_number('+998901234567')


