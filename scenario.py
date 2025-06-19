import re
url = "https://untrusted.example.com"
if re.match(r"https://example.com", url):
    pass
