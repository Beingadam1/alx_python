import requests
import sys


def main():
    # Checks if the script was provided with exactly one command-line argument
    if len(sys.argv) == 2:
        letter = sys.argv[
            1
        ]  # If a command-line argument is provided assigns it to the variable letter
    else:
        letter = ''  # Otherwise, set letter to an empty string

    payload = {
        'q': letter
    }  # Constructs a dictionary with the 'q' parameter set to the provided letter
    url = "http://0.0.0.0:5000/search_user"  # Sets the URL to which the POST request will be sent

    response = requests.post(
        url, data=payload
    )  # Sends a POST request to the specified URL with the payload

    try:
        json_data = response.json()  # Parse the JSON response body

        # Checks if the JSON is valid and not empty
        if json_data:
            user_id = json_data.get('id')  #  extracts the id
            user_name = json_data.get('name')  # Extract the name

            # Checks if both id and name are present
            if user_id is not None and user_name is not None:
                print(
                    "[{}] {}".format(user_id, user_name)
                )  # Prints them in the required format
            else:
                print("No result")  # If not present, print 'No result'
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")  # If the JSON is not valid, print "Not a valid JSON."


if __name__ == '__main__':
    main()
