from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='../.env')

DB_NAME = os.getenv('DB_NAME')
DB_KEY = os.getenv('DB_KEY')
