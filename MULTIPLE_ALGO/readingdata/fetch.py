# IMPORTING PACKAGES
##----------------------
import pandas as pd

# IMPORTING UDF
#----------------
import MULTIPLE_ALGO.logger.logger as lg

class csv_reader:

    @staticmethod
    def fetch_csv(file, frequency):

        try:
            # loading dataset
            data = pd.read_csv(file)

            # looging the loading dataset
            lg.App_logger.log("CSV file read Successfully !!")

            # Filter only first 2 columns
            data = data[[data.columns[0], data.columns[1]]]

            # converting the date column in to datetime
            data[data.columns[0]] = pd.to_datetime(data[data.columns[0]])

            # setting the date as index
            data.set_index(data.columns[0], inplace=True)

            # setting the frequency
            data=data.asfreq(str(frequency))

            # looging the loading dataset
            lg.App_logger.log("Returning the Dataframe !!")

            return data

        except Exception as e:
            lg.App_logger.log(str(e))


