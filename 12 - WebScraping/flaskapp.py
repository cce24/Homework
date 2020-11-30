from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Mission_to_Mars_Final

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/scrapemars")
# app.config["MONGO_URI"] = "mongodb://localhost:27017/scrapemars"
# mongo = PyMongo(app)


@app.route("/")
def home():
    usgs_dict = mongo.db.usgs_dict.find_one()
    return render_template("index.html", usgs=usgs_dict)


@app.route("/scrape")
def scraped():
    usgs_dict = mongo.db.usgs_dict
    usgs_dict_data = Mission_to_Mars_Final.scrape()
    usgs_dict.update({}, usgs_dict_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
