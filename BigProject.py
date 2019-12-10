#!flask/bin/python
from flask import Flask , jsonify, request, abort,  render_template, redirect, url_for, request
from musicDAO  import musicDAO # Link to DAO file

# Overide searching for a template folder when displaying pages (template_folder=""))
app = Flask(__name__,static_url_path ="",static_folder="", template_folder="")


# Once server is running open the login page... 
# http://127.0.0.1:5000/
@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # I have set the username and password here to admin
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            # If UN and PW are not true Print
            error = 'Invalid Credentials. Please try again.'
        else:
            # Send to index page of the site if UN and PW = True
            return render_template("/indexpage.html")
    return render_template("login.html", error=error)

# Get all pop that is in DAO and store in Var Result
@app.route("/pop")
def getAllPOP():
    results = musicDAO.getAllPOP()
    return jsonify(results)

@app.route("/pop/<int:id>")
def findByIdPOP(id): # Tested : curl "http://127.0.0.1:5000/pop/1"
    foundPOP = musicDAO.findByIdPOP(id)
    if not foundPOP:
         abort(404)
    return jsonify(foundPOP)

@app.route("/pop", methods=["POST"]) # Test :  curl -X POST "http://127.0.0.1:5000/pop"
def createPOP():
    global nextPOPArtistId
    if not request.json:
        abort(400)
    pop = {
        # "id": nextPOPArtistId,
        "artist": request.json["artist"],
        "album": request.json["album"],
        "price": request.json["price"]
    }
    addPOP = (pop["artist"], pop["album"], pop["price"])
    newID = musicDAO.createPOP(addPOP)
    pop["id"] = newID
    return jsonify(pop) # Tested : curl -i -H "Content-Type:application/json" -X POST -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":1000}" "http://127.0.0.1:5000/pop"

@app.route("/pop/<int:id>", methods=["PUT"]) # Tested : curl -X PUT "http://127.0.0.1:5000/pop/1"
def updatePOP(id):
    #foundPOP=list(filter(lambda p : p['id'] == id, popMusic))
    foundPOP = musicDAO.findByIdPOP(id)
    if not foundPOP:
        abort(404)
    if not request.json:
        abort(400)
    if "artist" in request.json and type(request.json["artist"]) != str:
        abort(400)
    if "album" in request.json and type(request.json["album"]) is not str:
        abort(400)
    if "price" in request.json and type(request.json["price"]) is not int:
        abort(400, description='price should be an int') # Display message when string is entered instead of int

    if "artist" in request.json: 
        foundPOP["artist"] = request.json["artist"]
    
    if "album" in request.json:
        foundPOP["album"] = request.json["album"]

    if "price" in request.json:
        foundPOP["price"] = request.json["price"]
    
    values = (foundPOP["artist"], foundPOP["album"], foundPOP["price"], foundPOP["id"])
    musicDAO.updatePOP(values)
    return jsonify(foundPOP) # Tested :  curl -i -H "Content-Type:application/json" -X PUT -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":10000}" "http://127.0.0.1:5000/pop/2"

@app.route("/pop/<int:id>", methods=["DELETE"]) # Tested : curl -X DELETE "http://127.0.0.1:5000/pop/1"
def deletePOP(id):
    musicDAO.deletePOP(id)
    return jsonify({"done":True})





# Music Rock ( CURL test was successful : curl "http://127.0.0.1:5000/rock" )
@app.route("/rock")
def getAllROCK():
    results= musicDAO.getAllROCK()
    return jsonify(results)


@app.route("/rock/<int:id>")
def findByIdROCK(id): # Tested : curl "http://127.0.0.1:5000/rock/1"
    #foundROCK = list(filter(lambda r: r['id'] == id, rockMusic))
    foundROCK = musicDAO.findByIdROCK(id)
    if not foundROCK:
         abort(404)
    return jsonify(foundROCK)


@app.route("/rock", methods=["POST"]) # Test :  curl -X POST "http://127.0.0.1:5000/rock"
def createROCK():
    global nextROCKArtistId
    if not request.json:
        abort(400)
    # Add other check
    rock = {
        #"id": nextROCKArtistId,
        "artist": request.json["artist"],
        "album": request.json["album"],
        "price": request.json["price"]
    }
    addROCK = (rock["artist"], rock["album"], rock["price"])
    newID = musicDAO.createROCK(addROCK)
    rock["id"] = newID
    return jsonify(rock) # Tested : curl -i -H "Content-Type:application/json" -X POST -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":1000}" "http://127.0.0.1:5000/rock"

@app.route("/rock/<int:id>", methods=["PUT"]) # Tested : curl -X PUT "http://127.0.0.1:5000/rock/1"
def updateROCK(id):
    foundROCK =  musicDAO.findByIdROCK(id)
    if not foundROCK:
        abort(404)
    if not request.json:
        abort(400)
    if "artist" in request.json and type(request.json["artist"]) != str:
        abort(400)
    if "album" in request.json and type(request.json["album"]) is not str:
        abort(400)
    if "price" in request.json and type(request.json["price"]) is not int:
        abort(400 ,description='price should be an int') # Display message when string is entered instead of int

    if "artist" in request.json: 
        foundROCK["artist"] = request.json["artist"]
    
    if "album" in request.json:
        foundROCK["album"] = request.json["album"]

    if "price" in request.json:
        foundROCK["price"] = request.json["price"]

    values = (foundROCK["artist"], foundROCK["album"], foundROCK["price"], foundROCK["id"])
    musicDAO.updateROCK(values)
    return jsonify(foundROCK) # Tested :  curl -i -H "Content-Type:application/json" -X PUT -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":10000}" "http://127.0.0.1:5000/rock/2"

@app.route("/rock/<int:id>", methods=["DELETE"]) # Tested : curl -X DELETE "http://127.0.0.1:5000/rock/1"
def deleteROCK(id):
    musicDAO.deleteROCK(id)
    return jsonify({"done":True})





# Music Disco ( CURL test was successful : curl "http://127.0.0.1:5000/disco/1" )
@app.route("/disco")
def getAllDISCO():
    results = musicDAO.getAllDISCO()
    return jsonify(results)

@app.route("/disco/<int:id>")
def findByIdDISCO(id): # # Tested : curl "http://127.0.0.1:5000/disco/1"
    foundDISCO = musicDAO.findByIdDISCO(id)
    if not foundDISCO:
         abort(404)
    return jsonify(foundDISCO)

@app.route("/disco", methods=["POST"]) # Test :  curl -X POST "http://127.0.0.1:5000/disco"
def createDISCO():
    global nextDISCOArtistId
    if not request.json:
        abort(400)
    disco = {
        #"id": nextDISCOArtistId,
        "artist": request.json["artist"],
        "album": request.json["album"],
        "price": request.json["price"]
    }

    addDISCO = (disco["artist"], disco["album"], disco["price"])
    newID = musicDAO.createDISCO(addDISCO)
    disco["id"] = newID
    return jsonify(disco) # Tested : curl -i -H "Content-Type:application/json" -X POST -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":1000}" "http://127.0.0.1:5000/disco"

@app.route("/disco/<int:id>", methods=["PUT"]) # Tested : curl -X PUT "http://127.0.0.1:5000/disco/1"
def updateDISCO(id):
    foundDISCO=musicDAO.findByIdDISCO(id)
    if not foundDISCO:
        abort(404)
    if not request.json:
        abort(400)
    if "artist" in request.json and type(request.json["artist"]) != str:
        abort(400)
    if "album" in request.json and type(request.json["album"]) is not str:
        abort(400)
    if "price" in request.json and type(request.json["price"]) is not int:
        abort(400 ,description='price should be an int') # Display message when string is entered instead of int

    if "artist" in request.json: 
        foundDISCO["artist"] = request.json["artist"]
    
    if "album" in request.json:
        foundDISCO["album"] = request.json["album"]

    if "price" in request.json:
        foundDISCO["price"] = request.json["price"]

    values = (foundDISCO["artist"], foundDISCO["album"], foundDISCO["price"], foundDISCO["id"])
    musicDAO.updateDISCO(values)
    return jsonify(foundDISCO) # Tested :  curl -i -H "Content-Type:application/json" -X PUT -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":10000}" "http://127.0.0.1:5000/disco/2"

@app.route("/disco/<int:id>", methods=["DELETE"]) # Tested : curl -X DELETE "http://127.0.0.1:5000/disco/1"
def deleteDISCO(id):
    musicDAO.deleteDISCO(id)
    return jsonify({"done":True})

if __name__=="__main__":
    app.run(debug= True)
