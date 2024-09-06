import requests
import json


class Telegraph():
    def __init__(self):
        self.Base_Api_URL = "https://api.telegra.ph/"

    def createAccount(self, short_name: str, author_name: str = "", author_url: str = "") -> dict:
        """
short_name (String, 1-32 characters) Required. Account name, helps users with several accounts remember which they are currently using. Displayed to the user above the "Edit/Publish" button on Telegra.ph, other users don't see this name.

author_name (String, 0-128 characters) Default author name used when creating new articles.

author_url (String, 0-512 characters) Default profile link, opened when users click on the author's name below the title. Can be any link, not necessarily to a Telegram profile or channel.
        """
        url: str = f"{self.Base_Api_URL}createAccount?short_name={short_name}"
        if author_name != "":
            url += f"&author_name={author_name}"
        if author_url != "":
            url += f"&author_url={author_url}"
        try:
            response = requests.get(url=url)
            response.raise_for_status()
            data: dict = response.json()

            if data.get("ok"):
                return data.get("result")
            else:
                return data.get("error")
        except requests.exceptions.RequestException:
            pass
        except ValueError:
            pass
        except KeyError:
            pass
            
    def editAccountInfo(self, access_token: str, short_name: str = "", author_name: str = "", author_url: str = "") -> dict:
        """
access_token (String) Required. Access token of the Telegraph account.

short_name (String, 1-32 characters) New account name.

author_name (String, 0-128 characters) New default author name used when creating new articles.

author_url (String, 0-512 characters) New default profile link, opened when users click on the author's name below the title. Can be any link, not necessarily to a Telegram profile or channel.
        """
        url: str = f"{self.Base_Api_URL}editAccountInfo?access_token={access_token}"
        if short_name != "":
            url += f"&short_name={short_name}"
        if author_name != "":
            url += f"&author_name={author_name}"
        if author_url != "":
            url += f"&author_url={author_url}"
        try:
            response = requests.get(url=url)
            response.raise_for_status()
            data: dict = response.json()

            if data.get("ok"):
                return data.get("result")
            else:
                return data.get("error")
        except requests.exceptions.RequestException:
            pass
        except ValueError:
            pass
        except KeyError:
            pass
            
    def getAccountInfo(self, access_token: str, fields: list = ["short_name", "author_name", "author_url"]) -> dict:
        """
access_token (String) Required. Access token of the Telegraph account.

fields (Array of String, default = [“short_name”,“author_name”,“author_url”]) List of account fields to return. Available fields: short_name, author_name, author_url, auth_url, page_count.
        """
        fields: str = json.dumps(fields)
        params: dict = {
            "access_token": access_token,
            "fields": fields
        }
        url: str = f"{self.Base_Api_URL}getAccountInfo"
        try:
            response = requests.get(url=url, params=params)
            response.raise_for_status()
            data: dict = response.json()

            if data.get("ok"):
                return data.get("result")
            else:
                return data.get("error")
        except requests.exceptions.RequestException:
            pass
        except ValueError:
            pass
        except KeyError:
            pass
            
    def revokeAccessToken(self, access_token: str):
        """
access_token (String) Required. Access token of the Telegraph account.
        """
        url: str = f"{self.Base_Api_URL}revokeAccessToken?access_token={access_token}"
        try:
            response = requests.get(url=url)
            response.raise_for_status()
            data: dict = response.json()

            if data.get("ok"):
                return data.get("result")
            else:
                return data.get("error")
        except requests.exceptions.RequestException:
            pass
        except ValueError:
            pass
        except KeyError:
            pass
