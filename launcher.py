# client import
from lib.client import client
# .env import
import os
from dotenv import load_dotenv
load_dotenv()
VERSION = 'main'
client.run(VERSION)
