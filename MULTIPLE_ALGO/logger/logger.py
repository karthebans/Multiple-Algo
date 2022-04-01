import os
from datetime import datetime


class App_logger:
    """
        This class shall  be used for logging the information.
        Version: 1.0
        Revisions: None
    """

    def log(log_message):
        """
            Method Name: log
            Description: This method for logging the information.
            Output: Writes in to Logs.txt.
            Version: 1.0
            Revisions: None
        """

        file_object = open("Log.txt", "a+")
        now = datetime.now()
        date = now.date()
        current_time = now.strftime("%H:%M:%S")
        file_object.write(str(date) + "/" + str(current_time) + "\t\t" + log_message + "\n")