import unittest
import pathlib as pl
from Databases import DB_handler as dbh


class TestDBHandler(unittest.TestCase):
    def test_Database_is_created(self):
        test_dbh = dbh.DBHandler
        test_dbh.create_table()
        path = pl.Path("Data_Job_Skills.db")
        self.assertEquals((str(path), path.is_file()), (str(path), True))
        path = pl.Path("Data_Staging_area.db")
        self.assertEquals((str(path), path.is_file()), (str(path), True))
        path = pl.Path("Job_Info.db")
        self.assertEquals((str(path), path.is_file()), (str(path), True))

    def test_Database_is_deleted(self):
        test_dbh = dbh.DBHandler
        test_dbh.delete_databases()
        path = pl.Path("Data_Job_Skills.db")
        self.assertEquals((str(path), path.is_file()), (str(path), False))
        path = pl.Path("Data_Staging_area.db")
        self.assertEquals((str(path), path.is_file()), (str(path), False))
        path = pl.Path("Job_Info.db")
        self.assertEquals((str(path), path.is_file()), (str(path), False))


if __name__ == '__main__':
    unittest.main()
