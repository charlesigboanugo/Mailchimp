matchDict = {
    "audience":[],
    "members":[],
    "tags":[],
    "segement":[],
    "campaigns":[],
    "signup":[],
    "automations":[],
    "templates":[],
    "facebookadd":[],
    "landingpage":[],
    "socialpost":[],
    "survey":[],
    "report":[],
}


async def getHelp(type: str = "full"):
    return
async def getReply(message: str, mailchimp):
    getHelp(type="hint")
    return getCampaigns()

async def getCampaigns():
    getHelp(type="getcamphint")
    return

async def getAudiences():
    getHelp(type="getaudhint")
    return

async def getSegments():
    getHelp(type="getseghint")
    return

async def getTags():
    getHelp(type="gettaghint")
    return

async def getAutomations():
    getHelp(type="getauthint")
    return

async def getTemplates():
    getHelp(type="gettemhint")
    return

async def getFaceAds():
    getHelp(type="getfachint")
    return

async def getLandings():
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

async def getSocials():
    getHelp(type="getsochint")
    return

async def getSurveys():
    getHelp(type="getsurhint")
    return

async def getReports():
    getHelp(type="getrephint")
    return