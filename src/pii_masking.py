"""
Privacy-Preserving Data Processing
Author: Sasibhushan Rao Chanthati
"""

import re


class PIIMasking:

    @staticmethod
    def mask_email(text):

        return re.sub(
            r'[\w\.-]+@[\w\.-]+',
            '[EMAIL_REDACTED]',
            text
        )

    @staticmethod
    def mask_phone(text):

        return re.sub(
            r'\d{3}-\d{3}-\d{4}',
            '[PHONE_REDACTED]',
            text
        )

    @staticmethod
    def mask_ssn(text):

        return re.sub(
            r'\d{3}-\d{2}-\d{4}',
            '[SSN_REDACTED]',
            text
        )


sample_text = """
John Doe
john@email.com
123-45-6789
"""

print(
    PIIMasking.mask_ssn(
        PIIMasking.mask_email(sample_text)
    )
)
