import os
from dotenv import load_dotenv
import base64

load_dotenv()

class Config:

    def __init__(self):
        self.url = os.getenv("OPENPROJECT_URL")

        self.user = os.getenv("OPENPROJECT_USER")
        self.password = os.getenv("OPENPROJECT_PASSWORD")

        self.api_version = "v3"
        self.api_base_url = f"{self.url}/api/{self.api_version}"

        self.token = os.getenv("TOKEN")


    def get_auth_headers(self) -> dict:
        encode_token = base64.b64encode(self.token.encode()).decode()
        return {
            "Authorization": f"Basic {encode_token}",
            "Content-Type": "application/json"
        } 

config = Config()


