matchDict = {
    "audience":{[""]},
    "members":{[], []},
    "tags":{[], []},
    "segement":{[], []},
    "campaigns":{[], []},
    "signup":{[], []},
    "automations":{[], []},
    "templates":{[], []},
    "facebookadd":{[], []},
    "landingpage":{[], []},
    "socialpost":{[], []},
    "survey":{[], []},
    "report":{[], []},
}


async def getHelp(type: str = "full"):
    result = ""
    if str != "full":
        for item in matchDict:
            for x in item:
                for y in x:
                    result + y + "\n"
    else:
        for item in matchDict[type]:
            for x in item:
                result + x + "\n"
    return result
       
async def reply(message: str, mailchimp):
    if type == 
    getHelp(type="hint")

async def Campaigns():
    getHelp(type="campaigns")
    return

async def Audiences():
    getHelp(type="getaudhint")
    return

async def Segments():
    getHelp(type="getseghint")
    return

async def Tags():
    getHelp(type="gettaghint")
    return

async def Automations():
    getHelp(type="getauthint")
    return

async def Templates():
    getHelp(type="gettemhint")
    return

async def FaceAds():
    getHelp(type="getfachint")
    return

async def Landings():
    getHelp(type="getlanhint")
    return

async def getCampaigns(mailchimp):
    try:
        response =  mailchimp.campaigns.list()
    except ApiClientError as err:
        return err.text
    campaigns = [item["settings"]["title"] for item in response["campaigns"]]
    campaigns = "\n".join(campaigns)
    return campaigns

async def Socials():
    getHelp(type="getsochint")
    return

async def Surveys():
    getHelp(type="getsurhint")
    return

async def Reports():
    getHelp(type="getrephint")
    return