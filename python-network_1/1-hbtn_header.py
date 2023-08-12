import requests
import sys


def main():
    url = sys.argv[1]
    req = requests.get(url)
    if 'X-Request-Id' in req.headers:
        reqValue = req.headers['X-Request-Id']
        print(reqValue)
    else:
        print("None")


if __name__ == '__main__':
    main()
