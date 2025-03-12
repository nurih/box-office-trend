import unittest
from day_query import create_query


class TestCreateQuery(unittest.TestCase):
    def test_well_formatted_is_ok(self):
        subject = "2025-02-03"
        _, param = create_query(subject)
        self.assertEqual(subject, param)

    def test_badly_formatted_throws(self):
        with self.assertRaises(ValueError):          
          create_query("1/2/2025")
    
    def test_rogue_sql_throws(self):
        with self.assertRaises(ValueError):          
          create_query("2025-04-01;DROP DATABASE admin;")
    

if __name__ == "__main__":
    unittest.main()
