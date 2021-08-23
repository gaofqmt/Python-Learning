# re built-in module

import re

# numbers >= 100 with optional leading zeros

print(re.findall(r'\b0*[1-9]\d{2,}\b', '0501 035 154 12 26 98234'))

# without raw strings
# \d is fine since there's no such escapse for normal strings
# \b is backspace in normal strings, whereas it is word boundary in regex

print(re.findall('\\b0*[1-9]\d{2,}\\b', '0501 035 154 12 26 98234'))