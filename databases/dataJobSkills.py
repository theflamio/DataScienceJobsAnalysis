import os
import sqlite3


class DataJobsSkill:

    @staticmethod
    def create_job_title_table() -> None:
        conn = sqlite3.connect("Data_Job_Skills.db")

        # create cursor
        c = conn.cursor()

        # create a table
        c.execute("""CREATE TABLE job_titles (
                job_title TEXT
            )""")

        c.execute("""CREATE TABLE companies (
                company_name TEXT
            )""")

        c.execute("""CREATE TABLE job_skills (
                job_skills TEXT
            )""")

        # Commit our command
        conn.commit()

        # Close our connection
        conn.close()

    @staticmethod
    def delete_databases() -> None:
        os.remove("Data_Job_Skills.db")
