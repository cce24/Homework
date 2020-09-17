#Import Dependencies
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Set Engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})

#Set Base
Base = automap_base()
Base.prepare(engine, reflect=True)

#Examine Base Keys
Base.classes.keys()

#Use Keys
Measurement = Base.classes.measurement
Station = Base.classes.station

#Bind Session to Python App and Database
session = Session(engine)

#Set Flask Weather App
app = Flask(__name__)

#Set Routes
@app.route("/")
def home():
    return (
            f"Available Routes:<br/>"
            f"/api/v1.0/precipitaton<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"

            f"/api/v1.0/<startDate><br/>"
            f"/api/v1.0//api/v1.0/<startDate>/<endDate><br/>")


#Set Last Date
last_date = (session.query(Measurement.date)
                .order_by(Measurement.date.desc())
                .first())
last_date = list(np.ravel(last_date))[0]
last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')

#Set Last Year
last_year = int(dt.datetime.strftime(last_date, '%Y'))

#Set Last Month
last_month = int(dt.datetime.strftime(last_date, '%m'))

#Set Last Day
last_day = int(dt.datetime.strftime(last_date, '%d'))

#Set Previous Year
prev_year = dt.date(last_year, last_month, last_day) - dt.timedelta(days=365)
prev_year = dt.datetime.strftime(prev_year, '%Y-%m-%d')



@app.route("/api/v1.0/precipitaton")
def precipitation():
    precipitation_results = (session.query(Measurement.date, Measurement.prcp, Measurement.station)
                      .filter(Measurement.date > prev_year)
                      .order_by(Measurement.date)
                      .all())
    
    precipitation = []
    for x in precipitation_results:
        precipitation_temp = {x.date: x.prcp, "Station": x.station}
        precipitation.append(precipitation_temp)

    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    station_results = session.query(Station.name).all()
    total_stations = list(np.ravel(station_results))
    return jsonify(total_stations)



@app.route("/api/v1.0/tobs")
def tobs():

    tobs_results = (session.query(Measurement.date, Measurement.tobs, Measurement.station)
                      .filter(Measurement.date > prev_year)
                      .order_by(Measurement.date)
                      .all())

    tobs = []
    for x in tobs_results:
        tobs_temp = {x.date: x.tobs, "Station": x.station}
        tobs.append(tobs_temp)

    return jsonify(tobs)

@app.route('/api/v1.0/<startDate>')
def start(startDate):
    sel = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    results =  (session.query(*sel)
                       .filter(func.strftime("%Y-%m-%d", Measurement.date) >= startDate)
                       .group_by(Measurement.date)
                       .all())

    selected_dates = []                       
    for result in results:
        date = {}
        date["Date"] = result[0]
        date["Low Temp"] = result[1]
        date["Avg Temp"] = result[2]
        date["High Temp"] = result[3]
        dates.append(date)
    return jsonify(selected_dates)




@app.route('/api/v1.0/<startDate>/<endDate>')
def startEnd(startDate, endDate):
    date_selection = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]


    start_end_results =  (session.query(*date_selection)
                       .filter(func.strftime("%Y-%m-%d", Measurement.date) >= startDate)
                       .filter(func.strftime("%Y-%m-%d", Measurement.date) <= endDate)
                       .group_by(Measurement.date)
                       .all())

    selected_dates = []                       
    for x in start_end_results:
        date = {}
        date["Date"] = x[0]
        date["Low Temp"] = x[1]
        date["Avg Temp"] = x[2]
        date["High Temp"] = x[3]
        selected_dates.append(date)
    return jsonify(selected_dates)

if __name__ == "__main__":
    app.run(debug=True)