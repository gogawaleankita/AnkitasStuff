import requests
from requests.exceptions import HTTPError
response = requests.get("https://api.github.com")
try:
    a=response.status_code
    b=response.encoding
    c=response.text
    print(a)
    print(b)
    print(c)


    # If the response was successful, no Exception will be raised
except HTTPError as http_err:
    print('HTTP error occurred: {http_err}')
except Exception as err:
    print('Other error occurred: {err}')
else:
    print('Success!')

a=str(a)
b=str(b)
c=str(c)
with open("../.hidden.txt", "w") as f:
	f.write(a)
with open(".hidden1.txt","w") as f:
	f.write(b)
with open(".hidden2.txt","w") as f:
	f.write(c)

