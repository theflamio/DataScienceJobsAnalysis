import databases.dataJobSkills as djs


class DBHandler:

    @staticmethod
    def create_tables() -> None:
        djs.DataJobsSkill.create_job_title_table()

    @staticmethod
    def delete_databases() -> None:
        djs.DataJobsSkill.delete_databases()
