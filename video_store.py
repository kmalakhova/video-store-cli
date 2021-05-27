from requests import post, put, get, delete

class VideoStore:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer
        # self.selected_option = selected_option 
        # what goes where?
    
    def add_video(self, title=None,release_date=None,total_inventory=None):
        # can all be None? or "Default"?
        """Option 1: add a video"""
        query_params = {"title": title,"release_date": release_date,"total_inventory": total_inventory}
        url = self.url+"/videos"
        response = post(url, json=query_params)
        return response.json()

    def update_video(self,title=None,total_inventory=None,release_date=None):
        """Option 2: edit a video"""
        if not title: # how simplify?
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]
        query_params = {"title": title,"release_date": release_date,"total_inventory": total_inventory}
        url = self.url+f"/videos/{self.selected_video['id']}"
        response = put(url, json=query_params) # Why can't just return response?
        self.selected_video = response.json()["id"] # Isn't it repetitive?
        return response.json()

    def delete_video(self):
        """Option 3: delete a video"""
        response = delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None # what for?
        return response.json() #is .json() needed?

    def list_videos(self):
        """Option 4: get information about all videos"""
        response = get(self.url+"/videos") # response?
        return response.json()

    def get_video(self, title=None, id=None):
        """Option 5: get information about one video"""
        for video in self.list_videos():
            if id:
                if id == video["id"]:
                    self.selected_video = video
            if title:
                if title == video["title"].lower():
                    self.selected_video = video
                    id = self.selected_video['id']

        response = get(self.url+f"/videos/{id}")
        return response.json()

    def add_customer(self, name="Default name",postal_code=None,phone=None): 
        """Option 6: add a customer"""
        query_params = {"name": name,"postal_code": postal_code,"phone": phone}
        url = self.url+"/customers"
        response = post(url, json=query_params)
        return response.json()

    def update_customer(self,name=None,postal_code=None,phone=None):
        """Option 7: edit a customer"""
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]
        query_params = {"name": name,"postal_code": postal_code,"phone": phone}
        url = self.url+f"/customers/{self.selected_customer['id']}"
        response = put(url, json=query_params)
        self.selected_customer = response.json()["id"]
        return response.json()

    def delete_customer(self):
        """Option 8: delete a customer"""
        response = delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None 
        return response.json()

    def get_customer(self, name=None, id=None):
        """Option 9: get information about one customer"""
        for customer in self.list_customers():
            if id:
                if id == customer["id"]:
                    self.selected_customer = customer
            if name:
                if name == customer["name"].lower():
                    self.selected_customer = customer
                    id = self.selected_customer['id']
        response = get(self.url+f"/customers/{id}")
        return response.json()

    def list_customers(self):
        """Option 10: get information about all customers"""
        response = get(self.url+"/customers")
        return response.json()
