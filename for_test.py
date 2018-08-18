from todoapp import app
import unittest
class flasktest(unittest.TestCase):

    #for showing all tasks

    def test_showall(self):
        tester=app.test_client(self)
        response=tester.get('/todo/v1_v01/tasks/api', content_type='application/json')
        self.assertEqual(response.status_code, 200)
    #for showing single task
    def test_find_one(self):
        tester=app.test_client(self)
        response=tester.get('/todo/v1_v01/tasks/api/01', content_type='application/json')
        self.assertEqual(response.status_code, 200)
    #for adding new task
    def test_adding(self):
        tester=app.test_client(self)
        response=tester.post('/todo/v1_v01/tasks/add', data={'ID':'04','Task':'5thtask','Description':'its the testing of api',
                                                             'Completion':False})
        self.assertEqual(response.status_code, 200)

    def testapiupdate(self):
        tester=app.test_client(self)
        response=tester.put('/todo/v1_v01/tasks/update/03', data={'ID':'03','Task':'3rd Task','Description':'its the testing of api',
                                                                  'Completion':True})
        self.assertEqual(response.status_code, 200)
    def test_deletion(self):
        tester=app.test_client(self)
        response=tester.delete('/todo/v1_v01/tasks/delete/03', content_type='application/json')
        self.assertEqual(response.status_code, 200)
if __name__=='__main__':
    unittest.main()
