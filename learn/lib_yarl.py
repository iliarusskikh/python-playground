#working with URLs
from yarl import URL

url = URL('https://example.com/path')
new_url =  url.with_path('/new-path').with_query({'key':'value'})
print(new_url)# https://example.com/new-path?key=value
