import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
USER = os.getenv('USER_NAME')
ADDRESS = os.getenv('ADDRESS')
EMAIL = os.getenv('EMAIL')

print(EMAIL)