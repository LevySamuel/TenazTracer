import requests
from bs4 import BeautifulSoup

def discover_user_on_social_networks(username):
    social_networks = ["twitter", "facebook", "instagram", "linkedin", "github"]
    user_links = []

    for site in social_networks:
        try:
            url = f"https://{site}.com/{username}"
            response = requests.get(url)

            if response.status_code == 200:
                user_links.append(url)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while checking {site}: {e}")

    return user_links

if __name__ == "__main__":
    username = input("Please enter your username: ")
    links = discover_user_on_social_networks(username)

    if links:
        print("Social Network Profile Links Found:")
        for link in links:
            print(link)
    else:
        print("No Social Network Profile Found for the Provided Username.")
