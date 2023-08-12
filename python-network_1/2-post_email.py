import requests
import sys


def main():
    url = sys.argv[1]  # Get the URL from the command-line argument
    email = sys.argv[2]  # Get the email that is the third param in the command line
    req = requests.post(
        url, data={'email': email}
    )  ## Send an HTTP POST request to the URL and The email must be sent in the variable email
    reqValue = req.text  # Set the text encoding of the response
    print(reqValue)  # Print the text


if __name__ == '__main__':
    main()
