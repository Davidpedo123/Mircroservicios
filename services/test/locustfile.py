from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def auth_token(self):
        # POST request
        self.client.post(
            url="/auth/token",
            headers={"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "password",
                "username": "user1",
                "password": "password1",
                "scope": "",
                "client_id": "string",
                "client_secret": "string"
            },
            verify=False
        )

    @task
    def get_user_monto(self):
        # GET request with Bearer token
        self.client.get(
            url="/user/monto",
            headers={
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSIsImV4cCI6MTcyOTc3NTY0NH0.SRZpBooHxs5hgR49-RuEz74svzVWFX1OHN1t8TTRwZo",
                "accept": "application/json"
            },
            verify=False
        )
