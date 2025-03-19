import os
print (os.environ)


# pathToFile = "text.txt"
# with open(pathToFile, "w") as file:
#     file.write("Hello, File!")
    
    
# with open(pathToFile, "r") as file:
#     print(file.read())


# yourMapName = dict()

# phonebook = dict()
# phonebook["Bob"] = "718-982-2800"

# bobsDigits = phonebook["Bob"]
# print(bobsDigits)

# initialString = '{"name": "john"}'

# import json
# formatted = json.loads(initialString)
# print(formatted["name"])
# import os
# os.system("python -m pip install requests")


# import requests

# response =  requests.get("https://google.com")
# if response.status_code  == 200:
#     print("Success!")
# elif response.status_code == 404:
#     print ("Not Found.")
    

import SimpleHTTPServer
import SocketServer

port = 8001

Handler = SimpleHTTPServer.SimpleHTTP

