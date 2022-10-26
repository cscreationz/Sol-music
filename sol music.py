import dropbox
from dotenv import load_dotenv
import os




print("Initializing Dropbox API...")
dbx = dropbox.Dropbox("<load_dotenv(API_KEY)>")
