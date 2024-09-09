import requests
import json


class Telegraph():
    def __init__(self):
        self.Base_Api_URL = "https://api.telegra.ph/"

    def createAccount(self, short_name: str,
                      author_name: str = None,
                      author_url: str = None) -> dict:
        """
short_name (String, 1-32 characters) Required. Account name, helps users with several accounts remember which they are currently using. Displayed to the user above the "Edit/Publish" button on Telegra.ph, other users don't see this name.
author_name (String, 0-128 characters) Default author name used when creating new articles.
author_url (String, 0-512 characters) Default profile link, opened when users click on the author's name below the title. Can be any link, not necessarily to a Telegram profile or channel.
        """
        url: str = f"{self.Base_Api_URL}createAccount?short_name={short_name}"
        if author_name is not None:
            url += f"&author_name={author_name}"
        if author_url is not None:
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
            
    def editAccountInfo(self, access_token: str,
                        short_name: str = None,
                        author_name: str = None,
                        author_url: str = None) -> dict:
        """
access_token (String) Required. Access token of the Telegraph account.
short_name (String, 1-32 characters) New account name.
author_name (String, 0-128 characters) New default author name used when creating new articles.
author_url (String, 0-512 characters) New default profile link, opened when users click on the author's name below the title. Can be any link, not necessarily to a Telegram profile or channel.
        """
        url: str = f"{self.Base_Api_URL}editAccountInfo?access_token={access_token}"
        if short_name is not None:
            url += f"&short_name={short_name}"
        if author_name is not None:
            url += f"&author_name={author_name}"
        if author_url is not None:
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
            
    def getAccountInfo(self, access_token: str,
                       fields: list = ["short_name", "author_name", "author_url"]) -> dict:
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

    def createPage(self, access_token: str,
                   title: str, content: list,
                   author_name: str = None, author_url: str = None,
                   return_content: bool = False) -> dict:
        """
access_token (String) Required. Access token of the Telegraph account.
title (String, 1-256 characters) Required. Page title.
author_name (String, 0-128 characters) Author name, displayed below the article's title.
author_url (String, 0-512 characters) Profile link, opened when users click on the author's name below the title. Can be any link, not necessarily to a Telegram profile or channel.
content (Array of Node, up to 64 KB) Required. Content of the page. 
return_content (Boolean, default = false) If true, a content field will be returned in the Page object (see: Content format).
        """
        url: str = f"{self.Base_Api_URL}createPage"
        parm: dict = {
            "access_token": access_token,
            "title": title,
            "content": json.dumps(content),
            "return_content": return_content
        }
        if author_name is not None:
            parm.update({"author_name": author_name})
        if author_url is not None:
            parm.update({"author_url": author_url})

        try:
            response = requests.post(url, data=parm)
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

    def editPage(self, access_token: str,
        path: str, title: str,
        content: list, author_name: str = None,
        author_url: str = None, return_content: bool = False
    ) -> dict:
        """
access_token (String) Required. Access token of the Telegraph account.
path (String) Required. Path to the page.
title (String, 1-256 characters) Required. Page title.
content (Array of Node, up to 64 KB) Required. Content of the page.
author_name (String, 0-128 characters) Author name, displayed below the article's title.
author_url (String, 0-512 characters) Profile link, opened when users click on the author's name below the title. Can be any link, not necessarily to a Telegram profile or channel.
return_content (Boolean, default = false) If true, a content field will be returned in the Page object.
        """
        url: str = f"{self.Base_Api_URL}editPage/{path}"
        parm: dict = {
            "access_token": access_token,
            "title": title,
            "content": json.dumps(content),
            "return_content": return_content
        }
        if author_name is not None:
            parm.update({"author_name": author_name})
        if author_url is not None:
            parm.update({"author_url": author_url})

        try:
            response = requests.post(url, data=parm)
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

    def getPage(self, path: str, return_content: bool =False) -> dict:
        """
path (String) Required. Path to the Telegraph page (in the format Title-12-31, i.e. everything that comes after https://telegra.ph/).
return_content (Boolean, default = false) If true, content field will be returned in Page object.
        """
        url: str = f"{self.Base_Api_URL}{path}?return_content={return_content}"
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

    def getPageList(self, access_token: str,
                    offset: int = 0, limit: int = 50) -> dict:
        """
access_token (String) Required. Access token of the Telegraph account.
offset (Integer, default = 0) Sequential number of the first page to be returned.
limit (Integer, 0-200, default = 50) Limits the number of pages to be retrieved.
        """
        url: str = f"{self.Base_Api_URL}getPageList?access_token={access_token}&offset={str(offset)}&limit={str(limit)}"
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
    
    def getViews(self, path:str, year: int,
                 month: int, day: int = None, hour: int = None) -> dict:
        """
path (String) Required. Path to the Telegraph page (in the format Title-12-31, where 12 is the month and 31 the day the article was first published).
year (Integer, 2000-2100) Required if month is passed. If passed, the number of page views for the requested year will be returned.
month (Integer, 1-12) Required if day is passed. If passed, the number of page views for the requested month will be returned.
day (Integer, 1-31) Required if hour is passed. If passed, the number of page views for the requested day will be returned.
hour (Integer, 0-24) If passed, the number of page views for the requested hour will be returned.
        """
        url: str = f"{self.Base_Api_URL}getViews/{path}?year={year}&month={month}"

        if day is not None:
            url += f"&day={day}"
        if hour is not None:
            url += f"&hour={hour}"
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
