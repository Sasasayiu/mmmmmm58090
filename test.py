from requests import post 
from fake_headers import Headers
import requests

data = post('https://discord.com/api/v9/auth/register/phone',json={"phone":"+79165885068"},proxies={'http://':'66.23.232.83:3128'})

print(data.text)