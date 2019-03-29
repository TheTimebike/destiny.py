import json

class Authorisation:
    def __init__(self, client):
        self.client = client
        self.tokens = {}

    def _save_tokens(self):
        with open("AuthTokens.json", "w+") as out:
            json.dump(self.tokens, out, indent=4)

    async def _load_tokens(self):
        with open("AuthTokens.json", "r+") as out:
            self.tokens = json.load(out)

        for key, attr in self.tokens.items():
            await self._get_access_from_refresh(attr["refresh_token"])

    async def _get_access_from_oauth(self, token):
        self._oauthToken = await self._request_access_from_oauth(token)
        self.tokens[self._oauthToken["membership_id"]] = self._oauthToken
        self._save_tokens()

    async def _get_access_from_refresh(self, token):
        self._oauthToken = await self._request_access_from_refresh(token)
        self.tokens[self._oauthToken["membership_id"]] = self._oauthToken
        self._save_tokens()

    async def _request_access_from_oauth(self, token):
        self._request = "https://www.bungie.net/platform/app/oauth/token/"
        self._headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self._data = "client_secret={1.auth.appSecret}&client_id={1.auth.appID}&grant_type=authorization_code&code={0}".format(token, self.client)
        self._response = await self.client.gatewaySession.post_request(self._request, self._headers, self._data)
        return self._response

    async def _request_access_from_refresh(self, token):
        self._request = "https://www.bungie.net/platform/app/oauth/token/"
        self._headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self._data = "client_secret={1.auth.appSecret}&client_id={1.auth.appID}&grant_type=refresh_token&refresh_token={0}".format(token, self.client)
        self._response =  await self.client.gatewaySession.post_request(self._request, self._headers, self._data)
        return self._response