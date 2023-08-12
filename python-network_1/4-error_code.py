import requests
import sys


def main():
    url = sys.argv[1]  # Get the URL from the command-line argument
    req = requests.get(url)  # Send an HTTP GET request to the URL

    # Check if the status code of the req is >= 400
    if req.status_code >= 400:
        print(f'Error code: {req.status_code}')  # prints Error otherwise print the body
    else:
        print(req.text)  # Print the body


if __name__ == '__main__':
    main()
