import unittest
import pathlib as pl
import databases.dBhandler as dbh


class TestDBHandler(unittest.TestCase):
    def test_Database_is_created(self):
        test_dbh = dbh.DBHandler
        test_dbh.create_tables()
        path = pl.Path("Data_Job_Skills.db")
        self.assertEqual((str(path), path.is_file()), (str(path), True))

    def test_Database_is_deleted(self):
        test_dbh = dbh.DBHandler
        test_dbh.delete_databases()
        path = pl.Path("Data_Job_Skills.db")
        self.assertEqual((str(path), path.is_file()), (str(path), False))
