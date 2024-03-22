import logging
from Scweet.user import get_users_following
from dotenv import load_dotenv
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Log the loading of environment variables
logging.info("Loaded environment variables from .env file")

# Assuming your Twitter credentials are stored in the .env file with these keys
env = {
    'SCWEET_EMAIL': os.getenv('SCWEET_EMAIL'),
    'SCWEET_USERNAME': os.getenv('SCWEET_USERNAME'),
    'SCWEET_PASSWORD': os.getenv('SCWEET_PASSWORD')
}

# Check if credentials are loaded
if not all(env.values()):
    logging.error("Missing one or more credentials in the environment variables.")
    exit()

# List of Twitter usernames to check their following
users = ['username1', 'username2', 'username3']

# Log the start of the following retrieval process
logging.info("Starting to retrieve following lists for specified users.")

# Call get_users_following function
# Adjust the 'wait' and 'limit' parameters as needed
try:
    following = get_users_following(users, env, headless=True, wait=2, limit=50)
    logging.info("Following lists have been successfully retrieved and saved.")
except Exception as e:
    logging.error("An error occurred while retrieving following lists: %s", str(e))

# Optionally, print or log the 'following' variable's contents if necessary
