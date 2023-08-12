import requests
import sys


def main():
    username = sys.argv[1]  # Get the username from the command-line argument
    password = sys.argv[2]  # Get the password from the command-line argument

    url = "https://api.github.com/user"  # # Set the URL to which the GET request will be sent
    response = requests.get(
        url, auth=(username, password)
    )  # Send a GET request to the specified URL with the username and password

    # Check if the response status is 200 (OK)
    if response.status_code == 200:
        user_data = response.json()  # Parse the JSON
        user_id = user_data.get('id')  # Get the user ID
        print(f'{user_id}')  # Print the User ID
    else:
        print('None')  # Print None if the statuse cose id not 200 (OK)


if __name__ == '__main__':
    main()
