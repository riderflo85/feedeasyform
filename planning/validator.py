import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_utensils(value):
    print('in validator')
    if type(value) == str:
        regex = re.compile(r"\w[=]\d[&]")
        print('in the validator', regex.search(value))
    else:
        raise ValidationError(
            _('%(value)s is not an even string'),
            params={'value': value}
        )