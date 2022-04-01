# IMPORTING PACKAGES
#----------------------
import pandas as pd
from pycaret.time_series import *
from pycaret.internal.pycaret_experiment import TimeSeriesExperiment

# IMPORTING UDF
#----------------
import MULTIPLE_ALGO.logger.logger as lg

class algorithm:

    @staticmethod
    def algo(data, forecast_period):
        try:
            # Initialing the pycaret setup
            exp = TimeSeriesExperiment()

            # feeding the data into the pycaret
            exp.setup(data, fh=3, fold=5, session_id=123, use_gpu=True)

            # logging the Initisation of pycaret setup
            lg.App_logger.log('Pycaret is initialised Successfully !!')

            # finding the best model
            best = exp.compare_models()

            # generate predictions
            final_best = exp.finalize_model(best)

            # logging the best model
            lg.App_logger.log("Found the best model !!")

            # making the dataframe
            df_results = pd.DataFrame(exp.predict_model(final_best, fh = int(forecast_period)))

            # logging the results
            lg.App_logger.log("Forecasting Results are converted into Dataframe !!")

            # returning the results
            return df_results

        except Exception as e:
            lg.App_logger.log(str(e))