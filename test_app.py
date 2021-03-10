import os
import unittest
import json
from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from app import app, create_app
from models import *


class CapstoneTestCase(unittest.TestCase):
    """This class represents the ___ test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.app = create_app(test_config=True)
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('test_user', 'test', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        

        # Test create_service    
        self.new_service = {
        "name":"Interpretation",
        "source":"EN",
        "destiny":"YN"
        }

        

    def tearDown(self):
        """Executed after reach test"""
        pass
    
    #-------------------------------------------
    # Unittest Handler GET request service
    #-------------------------------------------
    
    def test_get_services(self):
        res = self.client().get('/api/services')
    #    data = json.loads(res.data)
        print(str(res.status_code))

        self.assertEqual(res.status_code, 200)
        #self.assertEqual(data['success'], True)    
        # self.assertTrue(data['services'])
        # self.assertTrue(len(data['services']))

    # def test_404_not_found(self):
    #     res = self.client().get('/services/10000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Resource Not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
