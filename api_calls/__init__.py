from os import environ

from dotenv import load_dotenv
from requests import Session

BASE_URL = 'https://petstore.swagger.io/v2/'


__all__ = ('RS', BASE_URL)

load_dotenv()

RS = Session()
RS.auth = (environ.get('USERNAME'), environ.get('PASSWORD'))
