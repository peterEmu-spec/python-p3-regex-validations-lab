import re

# NAME: Must start with capital letters, allow:
# - single spaces between parts ("John Cena")
# - hyphens inside last names ("Taylor-Joy")
# - apostrophes ("D'Angelo")
# - NO empty string, NO lowercase-only names, NO numbers

name = r"^[A-Z][a-zA-Z]*(?:[ '-][A-Z][a-zA-Z]*)*$"
name_regex = re.compile(name)

# PHONE: Must match ONLY these:
# 5555555555
# 555-555-5555
# (555) 555-5555
# No double dashes, no letters, exactly 10 digits

phone_number = r"^(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

# EMAIL: Tests require:
# - must start with a letter (not a number)
# - letters, numbers, dots allowed before @
# - single @
# - domain with letters only
# - dot + letters only
# - no $, no missing domain

email_address = r"^[A-Za-z][A-Za-z0-9.]*@[A-Za-z]+\.[A-Za-z]+$"
email_regex = re.compile(email_address)
