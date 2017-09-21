import requests
import json
class user:
    """User class to have test cases for user """
    url = "https://reqres.in/api/users"
    name = ''
    job =''
    payload = {

    "name": name,
    "job": job
                }

    def case_list_user(self,page):
        flag =0
        """Method to test if user """
        url = self.url+"?page="+str(page)+""
        print url
        response = requests.get(url=url)
        print url
        print response.content

    def case_create_user(self,name,job):
        flag = 0
        """Case to create user a user and check if the user is created"""
        """case to create user with a correct data """
        print "\nRunning Test Case Create User "
        print "---------------------------------\n"
        self.payload['name']=name
        self.payload['job']=job

        print "\nName is -->" + self.payload['name']
        print "\nJob is -->" + self.payload['job']

        req_json = requests.post(url=self.url, data=self.payload)
        code = req_json.status_code
        data = json.loads(req_json.content)

        assert str(code) != 201,"Failed"
        print "\nStatus code is -->" + str(code)
        print "Response is " + str(data)
        assert data['name'] == name and data['job']== job,"Failed"
        print "\nCreate user with the ID "+ data['id']
        print "\nTest case Passed "
        print "\n\n---------------End of test case create user-----------------------------"


    def case_blank_name(self):
        flag = 0
        """case to create user with a blank name """
        print "\nRunning Test Case Blank Name "
        print "---------------------------------\n"
        print "Sending Blank name "
        self.payload['name'] = ""
        self.payload['job'] = "somethig"
        print "\nName is -->"+self.payload['name']
        print "\nJob is -->"+self.payload['job']
        req_json = requests.post(url=self.url, data=self.payload)
        code =req_json.status_code
        data = json.loads(req_json.content)
        assert code!=str(201),"Failed"
        print "\nStatus code is -->"+str(code)
        print "Response is " +str(data)
        if data['name']=='':
            flag = 0
        if flag == 0:
            print "\nCreate A user with blank name "
            print "\nTest case Failed "
        if flag == 1:
            print "\nCouldn't create user with a blank name"
            print "\nTest case Passed "


    def case_blank_job(self):
        """Case to create a user with blank Job"""
        flag = 0
        """case to create user with a blank JOB """
        print "\n\nRunning Test Case Blank JOB "
        print "---------------------------------\n"
        print "Sending Blank JOB "
        self.payload['name'] = "Ankit"
        self.payload['job'] = ""
        print "\nName is -->"+self.payload['name']
        print "\nJob is -->"+self.payload['job']
        req_json = requests.post(url=self.url, data=self.payload)
        code =req_json.status_code
        data = json.loads(req_json.content)
        assert str(code)!=201,"Falied"
        print "\nStatus code is -->"+str(code)
        print "Response is " +str(data)
        if data['job']=='':
            flag = 0
        if flag == 0:
            print "\nCreate A user with blank Job "
            print "\nTest case Failed "
        if flag == 1:
            print "\nCouldn't create user with a blank Job"
            print "\nTest case Passed "


    """Update user cases uing PUT call """

    def case_update_user(self,user_id,name,job):
        print "\nRunning Test case Update user  "
        print "---------------------------------\n"
        print "Sending payload "
        self.payload['name'] = name
        self.payload['job']=job
        print "\nName is -->"+self.payload['name']
        print "\nJob is -->"+self.payload['job']

        url = self.url+"/"+str(user_id)

        """CAse to update the user and check if its updated"""
        update_user = requests.put(url=url,data=self.payload)
        print update_user.content
        resp= json.loads(update_user.content)
        print resp
        if resp["name"]== name and resp['job']==job:
            print "\nUser Updated "
            print "\nTest case Pass"
        else:
            print "Test case fail"


    def update_case_blank_name(self,user_id):
        flag = 0
        print "\nRunning Test case update  blank name"
        print "---------------------------------\n"
        self.payload['name'] = ""
        self.payload['job']="test"
        url = self.url+"/"+str(user_id)
        """CAse to update the user and check if its updated"""
        update_user = requests.put(url=url,data=self.payload)
        print update_user.content
        data= json.loads(update_user.content)
        code = update_user.status_code
        print code
        assert str(code)!=200,"Failed"
        print "\nStatus code is -->"+str(code)
        print "Response is " +str(data)
        if data['name']=='':
            flag = 0
        if flag == 0:
            print "\nUpdated A user with blank Name "
            print "\nTest case Failed "
        if flag == 1:
            print "\nCouldn't update user with a blank Name"
            print "\nTest case Passed "


    def update_blank_job(self,user_id):
        flag = 0
        print "\n Test case  blank Job"
        print "---------------------------------\n"
        self.payload['name'] = "Ankit tiwari"
        self.payload['job'] = ""
        url = self.url + "/" + str(user_id)

        """CAse to update the user and check if its updated"""

        update_user = requests.put(url=url, data=self.payload)
        print update_user.content
        data = json.loads(update_user.content)
        code = update_user.status_code
        print code
        assert str(code) != 200,"Failed"
        print "\nStatus code is -->" + str(code)
        print "Response is " + str(data)
        if data['job'] == '':
            flag = 0
        if flag == 0:
            print "\nUpdated A user with blank Job "
            print "\nTest case Failed "
            print "\nCouldn't update user with a blank Job"
            print "\nTest case Passed "



    def delete_user(self,user_id):
        print "\nRunning Test case  Delete user "
        print "---------------------------------\n"
        url = self.url + "/" + str(user_id)
        del_user = requests.delete(url=url)
        print del_user.content
        mt =  del_user.status_code
        print mt
        assert str(mt) != 204,"Case Failed"

        print "Test case Delete user Passed"
