import os
from dotenv import load_dotenv


load_dotenv(override=True)


contacts = {
    "email": os.getenv("EMAIL"),
    "telegram": os.getenv("TELEGRAM"),
    "github": os.getenv("GITHUB"),
}
