# Import nessecary parts from flask and faker to generate random    # name and email.
from operator import ge
from flask import Flask, request, jsonify
from faker import Faker
import ApiFunctions
# To create and initialize a faker generator.
fake = Faker()
# Create the app object that will route our calls.
app = Flask(__name__)
# Add a single endpoint that we can use as an API to accept GET and # POST requests.
@app.route("/", methods=["POST", "GET"])
def index():
    # fake to create random name and email
    name = fake.name()
    email = fake.email()
    response = {
        "name": name,
        "email": email
    }
    # return name and email as a JSON httpresponse using jsonify
    return "Please add command"

@app.route("/getlocationbyname/<name>")
def getLocationByName(name):
    print("getting location by name")
    location = ApiFunctions.getLocationByName(name)
    print(location)
    response = {
        "location": location[0],
        "longandlat": location[1],
        "locationline": location[2]
    }
    print(jsonify(response))
    return jsonify(response)

# getLocationByName("Alfonso758")
@app.route("/getnamefromid/<id>")
def getNameFromID(id):
    
    name = ApiFunctions.getNameById(id) # get patient by name
    response = {
        "name": name
    }
    return jsonify(response)


# When run from command line, start the server.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')