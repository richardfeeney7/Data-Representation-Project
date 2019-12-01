#!flask/bin/python
from flask import Flask , jsonify, request, abort
#from flask_cors import CORS

app=Flask(__name__,static_url_path ="",static_folder="../")

# POP id is auto incrementing
# Tested :  curl "http://127.0.0.1:5000/pop"
popMusic=[
    {"id": 1, "artist":"Ariana Grande","album":"Thank U, Next","price":1500},
    {"id": 2, "artist":"Billie Eilish","album":"When We All Fall Asleep, Where Do We Go?","price":2500},
    {"id": 3, "artist":"Shawn Mendes","album":"Shawn Mendes","price":1000},
    {"id": 4, "artist":"Khalid","album":"Free Spirit","price":1799},
    {"id": 5, "artist":"Post Malone","album":"Hollywood's Bleeding","price":1500}
]
nextPOPArtistId=6

# ROCK id is auto incrementing
# Tested :  curl "http://127.0.0.1:5000/rock"
rockMusic=[
    {"id": 1, "artist":"Imagine Dragons","album":"Origins","price":1900},
    {"id": 2, "artist":"The Beatles","album":"Abbey Road","price":2000},
    {"id": 3, "artist":"Queen","album":"News of the World","price":1850},
    {"id": 4, "artist":"Portugal. The Man","album":" The Man Woodstock","price":1099},
    {"id": 5, "artist":"Foster The People","album":"Sacred Hearts Club","price":1100}
]
nextROCKArtistId=6

# DISCO id is auto incrementing
# Tested :  curl "http://127.0.0.1:5000/disco"
discoMusic=[
    {"id": 1, "artist":"Donna Summer","album":"Bad Girls","price":1350},
    {"id": 2, "artist":"Bee Gees","album":"Saturday Night Fever","price":2050},
    {"id": 3, "artist":"Village People","album":"Can't Stop the Music","price":2150},
    {"id": 4, "artist":"Diana Ross","album":"Eaten Alive","price":1159},
    {"id": 5, "artist":"Prince","album":"Purple Rain","price":1400}
]
nextDISCOArtistId=6


#@app.route("/")
#def index():
#    return "Hello, Richard!"

# Music Pop ( CURL test was successful : curl "http://127.0.0.1:5000/pop/1" )
@app.route("/pop")
def getAllPop():
    return jsonify(popMusic)

@app.route("/pop/<int:id>")
def findByIdPOP(id): # Tested : curl "http://127.0.0.1:5000/pop/1"
    foundPOP = list(filter(lambda p: p['id'] == id, popMusic))
    if len(foundPOP) == 0:
        return jsonify ({}) , 204
    return jsonify(foundPOP[0])

@app.route("/pop", methods=["POST"]) # Test :  curl -X POST "http://127.0.0.1:5000/pop"
def createPOP():
    global nextPOPArtistId
    if not request.json:
        abort(400)
    # Add other check
    pop = {
        "id": nextPOPArtistId,
        "artist": request.json["artist"],
        "album": request.json["album"],
        "price": request.json["price"]
    }
    nextPOPArtistId += 1
    popMusic.append(pop)
    return jsonify(popMusic) # Tested : curl -i -H "Content-Type:application/json" -X POST -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":1000}" "http://127.0.0.1:5000/pop"

@app.route("/pop/<int:id>", methods=["PUT"]) # Tested : curl -X PUT "http://127.0.0.1:5000/pop/1"
def updatePOP(id):
    foundPOP=list(filter(lambda p : p['id'] == id, popMusic))
    if len(foundPOP) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "artist" in request.json and type(request.json["artist"]) != str:
        abort(400)
    if "album" in request.json and type(request.json["album"]) is not str:
        abort(400)
    if "price" in request.json and type(request.json["price"]) is not int:
        abort(400, description='Price should be an int') # Display message when string is entered instead of int
    foundPOP[0]["artist"]  = request.json.get("artist",   foundPOP[0]["artist"])
    foundPOP[0]["album"]   = request.json.get("album",    foundPOP[0]["album"])
    foundPOP[0]["price"]   = request.json.get("price",    foundPOP[0]["price"])
    return jsonify( {"pop": foundPOP[0]}) # Tested :  curl -i -H "Content-Type:application/json" -X PUT -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":10000}" "http://127.0.0.1:5000/pop/2"

@app.route("/pop/<int:id>", methods=["DELETE"]) # Tested : curl -X DELETE "http://127.0.0.1:5000/pop/1"
def deletePOP(id):
    foundPOP=list(filter(lambda p: p['id']== id, popMusic))
    if (len(foundPOP) == 0):
        abort(404)
    popMusic.remove(foundPOP[0])
    return jsonify({"done":True})





# Music Rock ( CURL test was successful : curl "http://127.0.0.1:5000/rock/1" )
@app.route("/rock")
def getAllRock():
    return jsonify(rockMusic)

@app.route("/rock/<int:id>")
def findByIdROCK(id): # Tested : curl "http://127.0.0.1:5000/rock/1"
    foundROCK = list(filter(lambda r: r['id'] == id, rockMusic))
    if len(foundROCK) == 0:
        return jsonify ({}) , 204
    return jsonify(foundROCK[0])


@app.route("/rock", methods=["POST"]) # Test :  curl -X POST "http://127.0.0.1:5000/rock"
def createROCK():
    global nextROCKArtistId
    if not request.json:
        abort(400)
    # Add other check
    rock = {
        "id": nextROCKArtistId,
        "artist": request.json["artist"],
        "album": request.json["album"],
        "price": request.json["price"]
    }
    nextROCKArtistId += 1
    rockMusic.append(rock)
    return jsonify(rockMusic) # Tested : curl -i -H "Content-Type:application/json" -X POST -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":1000}" "http://127.0.0.1:5000/rock"

@app.route("/rock/<int:id>", methods=["PUT"]) # Tested : curl -X PUT "http://127.0.0.1:5000/rock/1"
def updateROCK(id):
    foundROCK=list(filter(lambda r : r['id'] == id, rockMusic))
    if len(foundROCK) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "artist" in request.json and type(request.json["artist"]) != str:
        abort(400)
    if "album" in request.json and type(request.json["album"]) is not str:
        abort(400)
    if "price" in request.json and type(request.json["price"]) is not int:
        abort(400 ,description='Price should be an int') # Display message when string is entered instead of int
    foundROCK[0]["artist"]  = request.json.get("artist",   foundROCK[0]["artist"])
    foundROCK[0]["album"]   = request.json.get("album",    foundROCK[0]["album"])
    foundROCK[0]["price"]   = request.json.get("price",    foundROCK[0]["price"])
    return jsonify( {"rock": foundROCK[0]}) # Tested :  curl -i -H "Content-Type:application/json" -X PUT -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":10000}" "http://127.0.0.1:5000/rock/2"

@app.route("/rock/<int:id>", methods=["DELETE"]) # Tested : curl -X DELETE "http://127.0.0.1:5000/rock/1"
def deleteROCK(id):
    foundROCK = list(filter(lambda r: r['id']== id, rockMusic))
    if (len(foundROCK) == 0):
        abort(404)
    rockMusic.remove(foundROCK[0])
    return jsonify({"done":True})





# Music Disco ( CURL test was successful : curl "http://127.0.0.1:5000/disco/1" )
@app.route("/disco")
def getAllDISCO():
    return jsonify(discoMusic)

@app.route("/disco/<int:id>")
def findByIdDISCO(id): # # Tested : curl "http://127.0.0.1:5000/disco/1"
    foundDISCO = list(filter(lambda d: d['id'] == id, discoMusic))
    if len(foundDISCO) == 0:
        return jsonify ({}) , 204
    return jsonify(foundDISCO[0])

@app.route("/disco", methods=["POST"]) # Test :  curl -X POST "http://127.0.0.1:5000/disco"
def createDISCO():
    global nextDISCOArtistId
    if not request.json:
        abort(400)
    disco = {
        "id": nextDISCOArtistId,
        "artist": request.json["artist"],
        "album": request.json["album"],
        "price": request.json["price"]
    }
    nextDISCOArtistId += 1
    discoMusic.append(disco)
    return jsonify(discoMusic) # Tested : curl -i -H "Content-Type:application/json" -X POST -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":1000}" "http://127.0.0.1:5000/disco"

@app.route("/disco/<int:id>", methods=["PUT"]) # Tested : curl -X PUT "http://127.0.0.1:5000/disco/1"
def updateDISCO(id):
    foundDISCO=list(filter(lambda r : r['id'] == id, discoMusic))
    if len(foundDISCO) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "artist" in request.json and type(request.json["artist"]) != str:
        abort(400)
    if "album" in request.json and type(request.json["album"]) is not str:
        abort(400)
    if "price" in request.json and type(request.json["price"]) is not int:
        abort(400 ,description='Price should be an int') # Display message when string is entered instead of int
    foundDISCO[0]["artist"]  = request.json.get("artist",   foundDISCO[0]["artist"])
    foundDISCO[0]["album"]   = request.json.get("album",    foundDISCO[0]["album"])
    foundDISCO[0]["price"]   = request.json.get("price",    foundDISCO[0]["price"])
    return jsonify( {"disco": foundDISCO[0]}) # Tested :  curl -i -H "Content-Type:application/json" -X PUT -d "{\"artist\":\"Richard\",\"album\":\"Test\",\"price\":10000}" "http://127.0.0.1:5000/disco/2"

@app.route("/disco/<int:id>", methods=["DELETE"]) # Tested : curl -X DELETE "http://127.0.0.1:5000/disco/1"
def deleteDISCO(id):
    foundDISCO = list(filter(lambda p: p['id']== id, discoMusic))
    if (len(foundDISCO) == 0):
        abort(404)
    discoMusic.remove(foundDISCO[0])
    return jsonify({"done":True})

if __name__=="__main__":
    app.run(debug= True)
