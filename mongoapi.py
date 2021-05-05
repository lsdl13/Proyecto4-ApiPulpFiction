from flask import Flask, request, jsonify, url_for, render_template
import tools.getdata as get
import json
import markdown.extensions.fenced_code
import tools.postdata as pos
import os

app=Flask(__name__)


@app.route("/")
def welcome():
    return '''
<!DOCTYPE html>
<html lang="en">
<center>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ironhack Sentiment Analysis</title>
</head>
<body style="background-color:#FFFFFF;">
<h1>Para obtener información sobre el guión de PulpFiction introduce uno de los siguientes endpoints.</h1>
</center>
<div class="block" style="float: right; width: 30%"> 
<h2>   Character Script Endpoints:<h2>
<ul>
    <li>distinct characters:(GET) /char</li>
    <li>script:(GET) /'char'</li>
</ul>
</div>
<div class="block" style="float: right; width: 30%">
<h2>   Place Script Endpoints:<h2>
<ul>
    <li>distinct places:(GET) /place</li>
    <li>script:(GET) /place/'place'</li>
</ul>
</div>
<div class="block" style="float: right; width: 30%">
</center>
<h2>   Time Script Endpoints:<h2>
<ul>
    <li>distinct daytimes:(GET) /time </li>
    <li>script:(GET) /time/'time'</li>
</ul>
</div>
<div style="clear: both"></div>
</dd>
<center>
<img src="https://cdn.culturagenial.com/es/imagenes/pulp-fiction-0-cke.jpg"/>
<form>
    <input type="button" value="Go back" onclick="history.back()">
</form>
</body>
</html>
'''


@app.route("/char")
def personaje(): 
    frases=get.get_char()
    return jsonify(frases)

@app.route("/<char>")
def frasespersonaje(char): 
    frases=get.get_char_script(char)
    return jsonify(frases)

@app.route("/time")
def time(): 
    frases=get.get_time()
    return jsonify(frases)

@app.route("/time/<time>")
def frasestime(time): 
    frases=get.get_time_script(time)
    return jsonify(frases)

@app.route("/place")
def place(): 
    frases=get.get_place()
    return jsonify(frases)

@app.route("/place/<place>")
def frasesplace(place): 
    frases=get.get_place_script(place)
    return jsonify(frases)


@app.route("/new/newscript", methods=["POST"])
def insert_line_():
    linenumber = request.form.get("Line number")
    character = request.form.get("Character")
    place = request.form.get("Place")
    time = request.form.get("Time")
    line = request.form.get("Line")
    wordcount = request.form.get("Word count")
    message = request.form.get("Message")
    pos.insert_line(linenumber, character, place, time, line, wordcount, message)
    return "Se ha introducido el mensaje en la base de datos"






















app.run(debug=True)