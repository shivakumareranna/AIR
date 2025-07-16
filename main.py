from dotenv import load_dotenv
from air import login, DistillerClient
import os

load_dotenv()  # This loads your ACCOUNT and API_KEY from your local '.env' file

account = os.environ["ACCOUNT"]
api_key = os.environ["API_KEY"]
user_id = account.replace("-", "_") + "_shivakumar_eranna"  # Replace 'test' by your Accenture ID
project = "gardening_project"
config_path = "config.yaml"

login(account, api_key)

distiller_client = DistillerClient()

distiller_client.create_project(
    config_path=config_path,
    project=project
)

response = distiller_client.interactive(
    project=project,
    uuid=user_id,
)
