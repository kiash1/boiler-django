import logging
from django.core.validators import RegexValidator

logger = logging.getLogger(__name__)


class PhoneRegexValidator(RegexValidator):
    regex = r"^(01\d{8,12}|\+?01\d{8,12})$"
    message = (
        "Phone number must be entered in the format: '+01xxxxxxxxx'. Maximum: 12 digits"
    )

    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)
        logger.debug(msg="Calling phone regex validator")
        logger.debug(msg=self.regex.search(str(*args)))