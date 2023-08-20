# Import the necessary libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup as bs  # For parsing HTML content

# Prompt the user to input their GitHub profile username
user_name = input("Enter your GitHub Profile Username: ")

# Construct the URL of the user's GitHub profile
url = "https://github.com/" + user_name

# Send an HTTP GET request to the GitHub profile URL
r = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = bs(r.content, "html.parser")

# Find the HTML element containing the user's profile image (avatar)
# The "alt" attribute of the <img> tag is set to "Avatar"
profile_image = soup.find("img", {"alt": "Avatar"})["src"]

# Print the URL of the user's profile image (avatar)
print(profile_image)
