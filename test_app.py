import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import app, create_app
from models import setup_db, Service

# -------------------------------------------
# Tokens
# -------------------------------------------

token_manager = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVudTVmRzc2NHRYM2RTeTBfU3A1UCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kLTIwMjEudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMDY0ZjNkMTUyMjE4MDA2YTNjYzEwMCIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjE2MDg1OTA2LCJleHAiOjE2MTYxNzIzMDYsImF6cCI6IkZxNjlTbTNMSTFRbDBKb3k4cmpVQ2VobTNlMk1xcHFSIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cGVyc29uIiwiZGVsZXRlOnByb2plY3QiLCJkZWxldGU6c2VydmljZSIsImdldDpwZXJzb24iLCJnZXQ6cGVyc29uLWRldGFpbCIsImdldDpwcm9qZWN0IiwiZ2V0OnByb2plY3QtZGV0YWlsIiwiZ2V0OnNlcnZpY2UtZGV0YWlsIiwicGF0Y2g6cGVyc29uIiwicGF0Y2g6cHJvamVjdCIsInBhdGNoOnNlcnZpY2UiLCJwb3N0OnBlcnNvbiIsInBvc3Q6cHJvamVjdCIsInBvc3Q6c2VydmljZSJdfQ.iivGCCVKDlTaAoQN7ScYbqCaimhrsv4TQ4jfXf0Q8ZuvoRuWv408HdgUNsWlbO8VknoJP8T4CESSj1js1F0BbXbM_13z4CJ8y2mnYNFHUQDmq034ZAeXD18ky-LEZ0OI-FSlZjZa7kvrx0j4dlUtPVeh1F8TFlHPE8lZ-NqmmautlaTdBmD1uhmpMKTh41rIR-LdTGIzk7XZP89SRmfhjg6YwfzT4qXYUkg0UcU0sCC1uqcTRRpL2Qmcnzwd4ydeYKlCP8Y0T0z4cf87hXL5KXOCxg6GGIHeiIPh7wjFOEtXocGe7559me-uQ_WQp1buYtOmanMamwXXftWzfYwE6A')
token_product_manager = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVudTVmRzc2NHRYM2RTeTBfU3A1UCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kLTIwMjEudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNDE3NDM5MGQ5ZjcxMDA3MGVlMmY3NSIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjE2MDc2OTQ3LCJleHAiOjE2MTYxNjMzNDcsImF6cCI6IkZxNjlTbTNMSTFRbDBKb3k4cmpVQ2VobTNlMk1xcHFSIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6cGVyc29uIiwiZ2V0OnBlcnNvbi1kZXRhaWwiLCJnZXQ6cHJvamVjdCIsImdldDpwcm9qZWN0LWRldGFpbCIsImdldDpzZXJ2aWNlLWRldGFpbCIsInBhdGNoOnBlcnNvbiIsInBhdGNoOnByb2plY3QiLCJwb3N0OnBlcnNvbiIsInBvc3Q6cHJvamVjdCJdfQ.iu9hKaTUK1LIu8FLpC61g7CUy8WT4ZqX1JcHgl5W4PZ7G67aKb2ZPsBgKhOKV_wFstHebT-lIeh6w9rC3pTyMtsUq9xm_LdRB55RaxbiFs7mO_H6fsacA46OjgZA1es3XHAWtUJoFG7ODSR4j91KSgr6Kb3uDb5q1pfUVBinHUy35lZMJRVExtNB3uJlGEU1UvGoz6Yin_neqvp89tqccZj2t2vumkX83D-zhWC0_omT0IdNSG-jl5mV0rYHaXbLUbb49JoRLmHV91Yi3z_TYbqaAUCG28fhoqLuhHuWzvcLwjiyfp7gWiMkf2g2ssZTOa6W3mzzaWCmp8D_hPMUIg')


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
            "name": "Translation",
            "source": "EN",
            "destiny": "JP"
        }

        # Test create_person
        self.new_person = {
            "name": "Pedro Hans",
            "kind": "Asign",
            "email": "pedro@example.com",
            "ratew": 0.02,
            "rateh": 10
        }

        # Test create_project
        self.new_project = {
            "name": "Project_test_2021",
            "kind": "Project",
            "deadline": "2011-03-02",
            "word_count": 50000,
            "hour_count": 10.0,
            "rate": 1000,
            "person_id": 1,
            "service_id": 1
        }
        pass

    def tearDown(self):
        """Executed after reach test"""
        pass

    # -------------------------------------------
    # Unittest Handler GET request service (Not permission needed)
    # -------------------------------------------

    def test_get_services(self):
        res = self.client().get('/api/services')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])
        self.assertTrue(len(data['services']))

    def test_404_service_fail_url(self):
        res = self.client().get('/api/servi')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')

    # -------------------------------------------
    # Unittest Handler GET request detail service ( Manager or PM role required)
    # -------------------------------------------

    def test_get_detail_service(self):
        res = self.client().get('/api/services/1', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['service'])
        self.assertTrue(len(data['service']))

    def test_404_service_not_found(self):
        res = self.client().get('/api/services/1000', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')

    def test_401_service_unauthorized_not_token(self):
        res = self.client().get('/api/services/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    # -------------------------------------------
    # Unittest Handler POST service ( Manager role required)
    # -------------------------------------------

    def test_create_service(self):
        res = self.client().post('/api/services', json=self.new_service, headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])

    def test_401_service_unauthorized_permission(self):
        res = self.client().post('/api/services', json=self.new_service, headers={'Authorization': 'Bearer ' + token_product_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # -------------------------------------------
    # Unittest Handler PATCH service ( Manager role required)
    # -------------------------------------------

    def test_update_service(self):
        res = self.client().patch('/api/services/2', json={
            "name": "Translation",
            "source": "English",
            "destiny": "Japanesse"},
            headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])

    def test_401_unauthorized_update_permission(self):
        res = self.client().patch('/api/services/2', json={
            "name": "Translation",
            "source": "English",
            "destiny": "Japanesse"}, headers={'Authorization': 'Bearer ' + token_product_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # -------------------------------------------
    # Unittest Handler Delete service ( Manager role required)
    # -------------------------------------------

    def test_delete_service(self):
        res = self.client().delete('/api/services/45', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])

    def test_401_unauthorized_service_delete_permission(self):
        res = self.client().delete('/api/services/4', headers={'Authorization': 'Bearer ' + token_product_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    # -------------------------------------------
    # Unittest Handler GET request people (Manager or PM role required)
    # -------------------------------------------

    def test_get_people(self):
        res = self.client().get('/api/people', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['people'])
        self.assertTrue(len(data['people']))

    def test_404_people_error_url(self):
        res = self.client().get('/api/peop', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')

    # -------------------------------------------
    # Unittest Handler GET request detail service (Manager or PM role required)
    # -------------------------------------------

    def test_get_detail_person(self):
        res = self.client().get('/api/people/2', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['person'])
        self.assertTrue(len(data['person']))

    def test_404_person_not_found(self):
        res = self.client().get('/api/people/a', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')

    # -------------------------------------------
    # Unittest Handler POST people (Manager or PM role required)
    # -------------------------------------------

    def test_create_person(self):
        res = self.client().post('/api/people', json=self.new_person, headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['people'])

    def test_405_if_person_creation_not_allowed(self):
        res = self.client().post('/api/people/45', json={
            "name": "Nora",
            "kind": "Asign",
            "email": "raquel@example.com",
            "ratew": 0.0,
            "rateh": 0.0},
            headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')

    # -------------------------------------------
    # Unittest Handler PATCH people (Manager or PM role required)
    # -------------------------------------------

    def test_update_person(self):
        res = self.client().patch('/api/people/2', json={
            "name": "Neil",
            "ratew": 0.05,
            "rateh": 10.0},
            headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['person'])

    def test_401_unauthorized_person_update_permission(self):
        res = self.client().patch('/api/people/2', json={
            "name": "Neil",
            "ratew": 0.01,
            "rateh": 15.0})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_person_to_update_not_found(self):
        res = self.client().patch('/api/people/10000', json={
            "name": "Neil",
            "ratew": 0.05,
            "rateh": 10.0},
            headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')
    # -------------------------------------------
    # Unittest Handler Delete people (Manager role required)
    # -------------------------------------------

    def test_delete_people(self):
        res = self.client().delete('/api/people/35', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['person'])

    def test_404_person_to_delete_not_found(self):
        res = self.client().delete('/api/people/1000', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')

    def test_401_unauthorized_delete_permission(self):
        res = self.client().patch('/api/people/4')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    # -------------------------------------------
    # Unittest Handler GET request project (Manager or PM role required)
    # -------------------------------------------

    def test_get_projects(self):
        res = self.client().get('/api/projects', headers={'Authorization': 'Bearer ' + token_product_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['projects'])
        self.assertTrue(len(data['projects']))

    def test_404_project_not_found(self):
        res = self.client().get('/api/projects/ads', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')

    # -------------------------------------------
    # Unittest Handler GET request detail project (Manager or PM role required)
    # -------------------------------------------

    def test_get_detail_project(self):
        res = self.client().get('/api/projects/1', headers={'Authorization': 'Bearer ' + token_product_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['project'])
        self.assertTrue(len(data['project']))

    def test_404_project_detail_not_found(self):
        res = self.client().get('/api/projects/1000', headers={'Authorization': 'Bearer ' + token_product_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')

    # -------------------------------------------
    # Unittest Handler POST projects (Manager or PM role required)
    # -------------------------------------------

    def test_create_projects(self):
        res = self.client().post('/api/projects', json=self.new_project, headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['projects'])

    def test_405_if_project_creation_not_allowed(self):
        res = self.client().post('/api/projects/45', json=self.new_project, headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')

    # -------------------------------------------
    # Unittest Handler PATCH project (Manager or PM role required)
    # -------------------------------------------

    def test_update_project(self):
        res = self.client().patch('/api/projects/1', json={
            "deadline": "2021-03-05",
            "word_count": 40000,
            "hour_count": 15.0,
            "rate": 10000
            },
            headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['project'])

    def test_401_unauthorized_project_update_permission(self):
        res = self.client().patch('/api/projects/1', json={
            "deadline": "2021-03-02",
            "word_count": 50000,
            "hour_count": 10.0,
            "rate": 1000
            })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # -------------------------------------------
    # Unittest Handler Delete projects (Manager role required)
    # -------------------------------------------

    def test_delete_projects(self):
        res = self.client().delete('/api/projects/27', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['projects'])

    def test_404_project_to_delete_not_found(self):
        res = self.client().delete('/api/projects/1000', headers={'Authorization': 'Bearer ' + token_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not found')

    def test_401_unauthorized_delete_project_permission(self):
        res = self.client().delete('/api/projects/3')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
