# IMPORTING PACKAGES
# ----------------------
import os

# IMPORTING UDF
# ----------------
import MULTIPLE_ALGO.logger.logger as lg
        
class makeResults:

    @staticmethod
    def return_data(df_results):

        try:
            # Saving the Results in CSV file
            df_results.to_csv('Pycaret_Prediction.csv')

            # logging the results created in CSV file
            lg.App_logger.log("CSV File created Successfully !!")

            # Creating csv file varibale
            csv_file = 'Pycaret_Prediction.csv'

            # Creating csv file path
            csv_path = os.path.join(os.getcwd(), 'Pycaret_Prediction.csv')

            # returning the path, csv_file, csv_path
            return csv_file, csv_path

        except Exception as e:
            lg.App_logger.log(str(e))