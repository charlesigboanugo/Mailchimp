import asyncio
import re

from mailchimp_marketing.api_client import ApiClientError
from mailchimp_marketing import Client

matchDict = {
    "lists":[["get lists", "get lists list_name"], ["add lists"]],
    "members":[["get campaigns"], ["add campaigns"]],
    "campaigns":[["get campaigns"], ["add campaigns"]],
    "automations":[["get automations"], ["add automations"]],
    "templates":[["get templates"], ["add template"]],
    "facebook_ads":[["get facebook_ads"], ["add facebookads"]],
    "landing_pages":[["get landing_pages"], ["add landing_pages"]],
}
"""
NOT IMPLEMENTED YET

"signups":[["get signups"], ["add signups"]],
"tags":[["get tags in audience_name"], ["add tags in audience_name"]],
"segments":[["get segements in audience_name"], ["add segements in audience_name"]],
"socialposts":[["get socialposts"], ["add socialposts"]],
"surveys":[["get surveys"], ["add surveys"]],
"reports":[["get reports"], ["add reports"]],

"""
async def help(help_type: str = "full", kind: int = 2):
    result = "Bad statement, see below for hints\n"
    if help_type == "full" and kind == 2:
        for item in matchDict:
            for x in matchDict[item]:
                for y in x:
                    result += y + "\n"
    elif kind == 2:
        for item in matchDict[help_type]:
            for x in item:
                result += x + "\n"
    else:
        if help_type == "full":
            for item in matchDict:
                for x in matchDict[item][kind]:
                    result += x + "\n"
        else:
            for item in matchDict[help_type][kind]:
                result += item + "\n"
    
    return result
       
async def reply(message: str, kind: int, mailchimp: Client):
    if message.strip == "":
        return await help(kind=kind)
    for key in matchDict.keys():
        if message.startswith(key):
            func = globals().get(key)
            message = message.replace(key, "").lstrip()
            return await func(message, kind, mailchimp)
    
    return await help(kind=kind)
            

async def campaigns(message: str, kind: int, mailchimp: Client):
    try:
        result = mailchimp.campaigns.list()
    except ApiClientError as err:
        return err.text
    camp = [item["settings"]["title"] for item in result["campaigns"]]
    if message == "":
        camp = "\n".join(camp)
        return camp
    elif message.startswith("in "):
        return 
    elif "in " in message.split():
        return
    elif message in [x.lower() for x in camp]:
        for item in result["campaigns"]:
            if item["settings"]["title"].lower() == message:
                return item["settings"]["title"]
    else:
        return await help(help_type="campaigns", kind=kind)
         
async def lists(message: str, kind: int, mailchimp: Client):
    try:
        result = mailchimp.lists.get_all_lists()
    except ApiClientError as err:
        return err.text
    lists = [item["name"] for item in result["lists"]]
    print(message)
    if message == "":
        lists = "\n".join(lists)
        return lists
    elif message in [x.lower() for x in lists]:
        for item in result["lists"]:
            if item["name"].lower() == message:
                return item["name"]
    else:
        return await help(help_type="lists", kind=kind)

async def automations(message: str, kind: int, mailchimp: Client):
    try:
        result = mailchimp.automations.list()
    except ApiClientError as err:
        return err.text
    auto = [item["settings"]["title"] for item in result["automations"]]
    if message == "":
        auto = "\n".join(auto)
        return auto
    elif message in [x.lower() for x in auto]:
        for item in result["automations"]:
            if item["settings"]["title"].lower() == message:
                return item["settings"]["title"]
    else:
        return await help(help_type="automations", kind=kind)

async def templates(message: str, kind: int, mailchimp: Client):
    try:
        result = mailchimp.templates.list()
    except ApiClientError as err:
        return err.text
    temp = [item["name"] for item in result["templates"]]
    if message == "":
        temp = "\n".join(temp)
        return temp
    elif message in [x.lower() for x in temp]:
        for item in result["templates"]:
            if item["name"] == message:
                return item["name"]
    else:
        return await help(help_type="templates", kind=kind)

async def facebook_ads(message: str, kind: int, mailchimp: Client):
    try:
        result = mailchimp.facebookAds.list()
    except ApiClientError as err:
        return err.text
    face = [item["ad_content"] for item in result["facebook_ads"]]
    if message == "":
        face = "\n".join(face)
        return face
    elif message in [x.lower() for x in face]:
        for item in result["facebook_ads"]:
            if item["ad_content"].lower() == message:
                return
    else:
        return await help(help_type="facebookads", kind=kind)

async def landing_pages(message: str, kind: int, mailchimp: Client):
    try:
        result = mailchimp.landingPages.get_all()
    except ApiClientError as err:
        return err.text
    land = [item["title"] for item in result["landing_pages"]]
    if message == "":
        land = "\n".join(land)
        return land
    elif message in [x.lower() for x in land]:
        for item in result["landing_pages"]:
            if item["title"].lower() == message:
                return item["title"]
    else:
        return await help(help_type="landing_pages", kind=kind)

"""async def socialposts(message: str, kind: int, mailchimp: Client):
    try:
        result = mailchimp
    except ApiClientError as err:
        return err.text
    lists = [item["settings"]["title"] for item in result["lists"]]
    if message == "":
        lists = "\n".join(lists)
        return lists
    elif message in lists:
        for item in result["lists"]:
            if item["settings"]["title"] == message:
                return
    else:
        return await help(help_type="lists", kind=kind)
"""
"""async def surveys(message: str, kind: int, mailchimp: Client):
    try:
        result = mailchimp
    except ApiClientError as err:
        return err.text
    lists = [item["settings"]["title"] for item in result["lists"]]
    if message == "":
        lists = "\n".join(lists)
        return lists
    elif message in lists:
        for item in result["lists"]:
            if item["settings"]["title"] == message:
                return
    else:
        return await help(help_type="lists", kind=kind)

async def reports(message: str, kind: int, mailchimp: Client):
    try:
        result =mailchimp.reports.get_all_campaign_reports()
    except ApiClientError as err:
        return err.text
    lists = [item["settings"]["title"] for item in result["lists"]]
    if message =="":
        lists = "\n".join(lists)
        return lists
    elif message in lists:
        for item in result["lists"]:
            if item["settings"]["title"] == message:
                return
    else:
        return await help(help_type="lists", kind=kind)

async def signups(message: str, kind: int, mailchimp: Client):
    if message == "" or not message.startswith("in"):
        return help
    else:
        aud = message[2:].lstrip()
        try:
            result =mailchimp.lists.list()
        except ApiClientError as err:
            return err.text
        lists = [item["settings"]["title"] for item in result["lists"]]

async def members(message: str, kind: int, mailchimp: Client):
    if message == "" or not message.startswith("in"):
        return help
    else:
        aud = message[2:].lstrip()
        try:
            result =mailchimp.lists.list()
        except ApiClientError as err:
            return err.text
        lists = [item["settings"]["title"] for item in result["lists"]]


async def segments(message: str, kind: int, mailchimp: Client):
    if message == "" or not message.startswith("in"):
        return help
    else:
        aud = message[2:].lstrip()
        try:
            result =mailchimp.lists.list()
        except ApiClientError as err:
            return err.text
        lists = [item["settings"]["title"] for item in result["lists"]]


async def tags(message: str, kind: int, mailchimp: Client):
    if message == "" or not message.startswith("in"):
        return help
    else:
        aud = message[2:].lstrip()
        try:
            result =mailchimp.lists.list()
        except ApiClientError as err:
            return err.text
        lists = [item["settings"]["title"] for item in result["lists"]]

"""

async def processResult(message: str, settings: list[str]):
    
    mailchimp = Client()

    MAILCHIMP_KEY = None
    for item in settings:
        if item["label"] == "api key":
            MAILCHIMP_KEY = item["default"]
    if MAILCHIMP_KEY is None:
            return "you need to add your mailchimp api key in the app settings"
    mailchimp.set_config({
    "api_key": MAILCHIMP_KEY,
    "server": "us14"
    })
    message = re.sub(r'</?p>', '', message)
    message = message.lstrip().lower()
    if message.startswith("get"):
        message = " ".join(message[3:].split())
        result = await reply(message, 0, mailchimp)
        return result
    elif message.startswith("add"):
        message = " ".join(message[3:].split())
        result = await reply(message, 1, mailchimp)
        return result
    else:
         result = await help(help_type="full")
         return result

async def inHtml(result: str):
    result = f"<div style='border-left: solid green 7px; padding: 20px;"
    f"background-color: #090909; line-height: 2; width: 80%;"
    f"color: white;'><h1 style='font-size: 2Opx;'>Response<h1>\n"
    f"<p style='font-size:16;'>{result}</p><div>"
    return result