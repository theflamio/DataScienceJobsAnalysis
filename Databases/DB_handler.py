import os
import sqlite3


class DBHandler:

    @staticmethod
    def create_table() -> None:
        # create/connect to db
        conn1 = sqlite3.connect("Data_Staging_area.db")
        conn2 = sqlite3.connect("Data_Job_Skills.db")
        conn3 = sqlite3.connect("Job_Info.db")

        # Close our connection
        conn1.close()
        conn2.close()
        conn3.close()

    @staticmethod
    def delete_databases() -> None:
        os.remove("Data_Staging_area.db")
        os.remove("Data_Job_Skills.db")
        os.remove("Job_Info.db")