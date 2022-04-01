# IMPORTING LIBRARIES :
# --------------------
import os
from flask_cors import CORS, cross_origin
from flask import Flask, request, send_file, send_from_directory

# IMPORTING UDF LIBRARIES OF MULTIPLE ALGO:
# -----------------------------------------
from MULTIPLE_ALGO.readingdata.fetch import csv_reader
from MULTIPLE_ALGO.pycaretudf.pycaretforecast import algorithm
from MULTIPLE_ALGO.makedir.compileforecast import makeResults
import MULTIPLE_ALGO.logger.logger as lg

app = Flask(__name__)
CORS(app)


@app.route('/Multiple_Algo', methods = ['POST', 'GET'])
@cross_origin(origin = '*')
def pycaret():

    file = request.files['file']
    lg.App_logger.log("File Received from the User !!")
    if file:
        pass
    else:
        return "FILE NOT UPLOADED !! PLEASE UPLOAD FILE !!" 
    if file.filename.split('.')[1] != 'csv':
        return "Please Upload a CSV file."

    frequency = request.form['frequency']
    lg.App_logger.log("Frequency Received from the User !!")
    if frequency:
        pass
    else:
        return "FREQUENCY NOT GIVEN / ENTERED !!"

    forecast_period = request.form['forecast_period']
    lg.App_logger.log("Forecast Period Received from the User !!")
    if forecast_period:
        pass
    else:
        return "FORECAST PERIOD VALUE NOT GIVEN / ENTERED !!"
    
    data = csv_reader.fetch_csv(file, frequency)
    df_results = algorithm.algo(data, forecast_period)
    csv_file, csv_path = makeResults.return_data(df_results)

    # Also make sure the requested csv file does exist
    if not os.path.isfile(csv_path):
        lg.App_logger.log("ERROR: file %s was not found on the server" % csv_file)

    # Send the forecasted values in CSV file to the user
    return send_file(path_or_file=csv_path, as_attachment=True, attachment_filename=csv_file)


if __name__ == '__main__':
    app.run(host = "0.0.0.0",port=8091, debug=True )