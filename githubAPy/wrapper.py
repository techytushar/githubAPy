import requests
import json
import base64


class gapy:

    error_message = """Error occured while processing the request."""

    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            "Accept":"application/vnd.github.machine-man-preview+json",
            "Authorization":"bearer "+self.access_token,
            "Content-Type":"application/json",
        }
        self.url = "https://api.github.com/"
        self.me = self.get_me()
        self.username = self.me["login"]

    def get_me(self):
        """ Returns the user's info """
        endpoint = self.url+'user'
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(self.error_message)

    def user(self, username):
        """ Return info of a GitHub user """
        endpoint = self.url+'users/{}'.format(username)
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(self.error_message)
    
    def create_fork(self, owner, repo):
        """ Creates fork of a repo """
        endpoint = self.url+'repos/{}/{}/forks'.format(owner, repo)
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            for fork in data:
                """ Check if fork already exists """
                if(fork["owner"]["login"]==self.username):
                    return fork["html_url"]
            else:
                """ If user has not forked the repo """
                response = requests.post(endpoint, headers=self.headers)
                if response.status_code == 202:
                    return json.loads(response.text)['html_url']
                raise Exception(self.error_message)
        raise Exception(self.error_message)
    
    def update_with_upstream(self, owner, repo):
        """ Updates forked repo with upstream master """
        update_url = self.url+"repos/{}/{}/git/refs/heads/master".format(owner, repo)
        response = requests.get(update_url, headers=self.headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            sha = data["object"]["sha"]
            body = {
                "sha":sha,
                "force": True
            }
            endpoint = self.url+"repos/{}/{}/git/refs/heads/master".format(self.username, repo)
            response = requests.patch(update_url, headers=self.headers, data=json.dumps(body))
            if response.status_code==200:
                return True
            raise Exception(self.error_message)
        raise Exception(self.error_message)
    