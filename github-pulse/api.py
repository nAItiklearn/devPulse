import requests

class gitHubClient:
    baseURL = "https://api.github.com"
    
    def __init__(self):
        self.sessions = requests.Session()
        self.sessions.headers.update({
           "Accept": "application/vnd.github+json" 
        })
    
    def get(self, endpoint ,params=None ):
        """1-send a GET request to gh api
           2-api returns list:JSON response
           raiee exception if GH throws error"""
        url = self.baseURL +endpoint
        response = self.session.get(
            url,
            params=params
        )
        response.raise_for_status()
        return response.json()
    
    def get_user(self, username):
        return self.get(f"/users/{username}") #get info abt github user
    
    def get_repos(self , username): #get repo names
        return self.get(f"/users/{username}/repos",params={"per_page":100, "sort": "updated"})
    
    def get_repo(self, owner , repo):
        #get detailed info about a repo
        return self.get(f"/repos/{owner}/{repo}")
    
    def get_languages_used(self, owner , repo):
        return self.get(f"/repos/{owner}/{repo}/languages")
    
    def get_commits(self, owner, repo):
        #no of commits 
        return self.get(f"/repos/{owner}/{repo}/commits", params={"per_page":100})
    
        
    
        
           
        