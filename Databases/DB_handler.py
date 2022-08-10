import Data_Job_Skills


class DBHandler:

    @staticmethod
    def create_tables() -> None:
        Data_Job_Skills.DataJobsSkill.create_job_title_table()

    @staticmethod
    def delete_databases() -> None:
        Data_Job_Skills.DataJobsSkill.delete_databases()



