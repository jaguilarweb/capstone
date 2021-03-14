import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import app, create_app
from models import setup_db, Service

# Tokens
token_manager=('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVudTVmRzc2NHRYM2RTeTBfU3A1UCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kLTIwMjEudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMDY0ZjNkMTUyMjE4MDA2YTNjYzEwMCIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjE1Njc5Mzc0LCJleHAiOjE2MTU2ODY1NzQsImF6cCI6IkZxNjlTbTNMSTFRbDBKb3k4cmpVQ2VobTNlMk1xcHFSIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cGVyc29uIiwiZGVsZXRlOnByb2plY3QiLCJkZWxldGU6c2VydmljZSIsImdldDpwZXJzb24iLCJnZXQ6cGVyc29uLWRldGFpbCIsImdldDpwcm9qZWN0IiwiZ2V0OnByb2plY3QtZGV0YWlsIiwiZ2V0OnNlcnZpY2UtZGV0YWlsIiwicGF0Y2g6cGVyc29uIiwicGF0Y2g6cHJvamVjdCIsInBhdGNoOnNlcnZpY2UiLCJwb3N0OnBlcnNvbiIsInBvc3Q6cHJvamVjdCIsInBvc3Q6c2VydmljZSJdfQ.DmGolqeGaFGbwguL_SKLM1Iy_iizc03JWb0UZIyN8y0ZrTSHpGF1JG2_p1zspOhv8R43uI1zZhlqpf7J1m2-V8Nzu2YT5U8SHaLNhpY-IYzajqq9um6VDvB3_VTMtRwqL7RwifdV6MTV95Y8uvI-JE-HYJA9BnlQ0B6YAMPIU2CRp2gbJK2r-6_TKXyglmJ73HuzkQiWyUCLSiN63dDjVxFmxbmjx2sTP4SseJU4LU1FZ5h1Iv5mNY9WNLQ5DmXsgbA8Ka3SjsmXkIE69J4ZCSB668w9NTijRyVAgTmZ3MBQo--gO623pJ-71Be9tYnrAx2TWglVJi720cnZA6A_sA')
token_product_manager=('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVudTVmRzc2NHRYM2RTeTBfU3A1UCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kLTIwMjEudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNDE3NDM5MGQ5ZjcxMDA3MGVlMmY3NSIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjE1Njc3MDc4LCJleHAiOjE2MTU2ODQyNzgsImF6cCI6IkZxNjlTbTNMSTFRbDBKb3k4cmpVQ2VobTNlMk1xcHFSIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6cGVyc29uIiwiZ2V0OnBlcnNvbi1kZXRhaWwiLCJnZXQ6cHJvamVjdCIsImdldDpwcm9qZWN0LWRldGFpbCIsImdldDpzZXJ2aWNlLWRldGFpbCIsInBhdGNoOnBlcnNvbiIsInBhdGNoOnByb2plY3QiLCJwb3N0OnBlcnNvbiIsInBvc3Q6cHJvamVjdCJdfQ.HzyvKn3HljWVKyNGyh7lWtbeMKzZsbd1VCh3Yl4wXSFBPz2SVDY6ulHg8dRi5Ceqe_MgWpQxx5BFUuPJeIurImfa_V4nJ0Xx8CTyM18BAA1ckYueT-W_zed1XeohAdG-V7G7qTMNZPIQt2-ZaTJ-LUZaCkoaa5lQd3J9P5sEQNryBwsdk_bM1M4s7cerU_5XdoH4ta74T82Rvko4591lPuofHZSLA__YHkW4YkSbbIW2J8GIe1puNZu1IHufz2KsOK5Y-QuVgd4NEis0odRA_0p84kYGjyYvcYUKwl-WwCqGSze6y1XTrs2gecU3ROJKurJm3ufAdVxzHTCjt6sy9g')

class CapstoneTestCase(unittest.TestCase):
    """This class represents the ___ test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('test_user', 'test', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        
        # Binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # Test create_service    
        self.new_service = {
        "name":"Translation",
        "source":"EN",
        "destiny":"JP"
        }        
        pass

    def tearDown(self):
        """Executed after reach test"""
        pass
    
    #-------------------------------------------
    # Unittest Handler GET request service (Not permission needed)
    #-------------------------------------------
    
    def test_get_services(self):
        res = self.client().get('/api/services')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])
        self.assertTrue(len(data['services']))

    def test_404_not_found(self):
        res = self.client().get('/api/servi')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')
    
    #-------------------------------------------
    # Unittest Handler GET request detail service ( Manager or PM role required)
    #-------------------------------------------
    
    def test_get_detail_service(self):
        res = self.client().get('/api/services/1', headers={'Authorization': 'Bearer '+ token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['service'])
        self.assertTrue(len(data['service']))

    def test_404_service_not_found(self):
        res = self.client().get('/api/services/1000', headers={'Authorization': 'Bearer '+ token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')
        
    def test_401_unauthorized_not_token(self):
        res = self.client().get('/api/services/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_401_unauthorized_false_token(self):
        res = self.client().get('/api/services/2', headers={'Authorization': 'Bearer ' + 'false_token'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')
    #-------------------------------------------
    # Unittest Handler POST service ( Manager role required)
    #-------------------------------------------

    def test_create_service(self):
        res = self.client().post('/api/services', json=self.new_service, headers={'Authorization': 'Bearer '+ token_manager})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])
    
    def test_401_unauthorized_permission(self):
        res = self.client().post('/api/services', json=self.new_service, headers={'Authorization': 'Bearer '+ token_product_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')


    #-------------------------------------------
    # Unittest Handler PATCH service ( Manager role required)
    #-------------------------------------------

    def test_update_service(self):
        res = self.client().patch('/api/services/1', json={
        "name":"Translation",
        "source":"English",
        "destiny":"Japanesse"}, 
        headers={'Authorization': 'Bearer '+ token_manager})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])
    

    def test_401_unauthorized_update_permission(self):
        res = self.client().patch('/api/services/1', json={
        "name":"Translation",
        "source":"English",
        "destiny":"Japanesse"},
        headers={'Authorization': 'Bearer '+ token_product_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')
        
    #-------------------------------------------
    # Unittest Handler Delete service ( Manager role required)
    #-------------------------------------------

    def test_delete_service(self):
        res = self.client().delete('/api/services/4',
        headers={'Authorization': 'Bearer '+ token_manager})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])
    
    def test_404_service_not_found(self):
        res = self.client().delete('/api/services/100',
        headers={'Authorization': 'Bearer '+ token_manager})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')
    
    def test_401_unauthorized_delete_permission(self):
        res = self.client().patch('/api/services/4',
        headers={'Authorization': 'Bearer '+ token_product_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')

        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

