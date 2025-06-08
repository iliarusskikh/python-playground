"""
Common values include:
application/json: JSON data (used by JSONPlaceholder and most REST APIs).
text/plain: Plain text.
text/html: HTML content (e.g., a web page).
application/xml: XML data.
image/png: Binary image data.
multipart/form-data: Form data with multiple parts (e.g., file uploads).

The charset parameter (e.g., charset=utf-8) specifies the character encoding, ensuring correct text interpretation.
"""


"""
If Content-Type: application/json, use response.json().
If Content-Type: text/plain, use response.text.
If Content-Type: image/png, treat response.content as binary data.

"""


if 'application/json' in response.headers['content-type'].lower():
    data = response.json()
else:
    print(f"Unexpected Content-Type: {response.headers['content-type']}")
