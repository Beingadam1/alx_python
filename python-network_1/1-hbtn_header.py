import requests
import sys


def main():
    url = sys.argv[1]  # Get the URL from the command-line argument
    req = requests.get(url)  # Send an HTTP GET request to the URL

    # Check if the 'X-Request-Id' header is present in the response headers
    if 'X-Request-Id' in req.headers:
        reqValue = req.headers['X-Request-Id']  # Get the value of 'X-Request-Id' header
        print(reqValue)  # Print the value of 'X-Request-Id' header
    else:
        print('None')  # If 'X-Request-Id' header is not present, print "None"


if __name__ == '__main__':
    main()
