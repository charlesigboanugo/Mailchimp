matchDict = {
    "audiences":[[""][]],
    "members":[[], []],
    "tags":[[], []],
    "segments":[[], []],
    "campaigns":[[], []],
    "signups":[[], []],
    "automations":[[], []],
    "templates":[[], []],
    "facebookads":[[], []],
    "landingpages":[[], []],
    "socialposts":[[], []],
    "surveys":[[], []],
    "reports":[[], []],
}

async def help(help_type: str = "full", kind: int = 2):
    result = "Bad statement, see below for hints\n"
    if help_type == "full" && kind == 2:
        for item in matchDict:
            for x in item:
                for y in x:
                    result + y + "\n"
    elif kind == 2:
        for item in matchDict[help_type]:
            for x in item:
                result + x + "\n"
    else:
        if help_type == "full":
            for item in matchDict:
                for x in item[kind]
                    result + x + "\n"
        else:
            for item in matchDict[help_type][kind]
                result + item + "\n"

    return result
       
async def reply(message: str, kind: int, mailchimp):
    if any(message.startswith(key) for key in matchDict.keys()):
        func = globals().get(key)
        message = message.replace(key, "").lstrip()
        return await func(message, kind, mailchimp)
    else:
        return help(kind=kind)
            

async def campaigns(message, mailchimp, kind):
    try:
        response =  await mailchimp.audiences.list()
    except ApiClientError as err:
        return err.text
    audiences = [item["settings"]["title"] for item in response["audiences"]]
    if message = ""
        audiences = "\n".join(audiences)
        return audiences

    elif message.startswith("in"):

    elif "in" in messages.split():
            check for campaign with audience else return err
    elif message in audiences:
        for item in response["audiences"]:
            if item["settings"]["title"] == message:
                return
    else:
        return help(help_type="audiences", kind=kind)
         
async def audiences(message, kind, mailchimp):
    try:
        response =  await mailchimp.audiences.list()
    except ApiClientError as err:
        return err.text
    audiences = [item["settings"]["title"] for item in response["audiences"]]
    if message = ""
        audiences = "\n".join(audiences)
        return audiences
    elif message in audiences:
        for item in response["audiences"]:
            if item["settings"]["title"] == message:
                return
    else:
        return help(help_type="audiences", kind=kind)

async def automations():
    try:
        response =  await mailchimp.audiences.list()
    except ApiClientError as err:
        return err.text
    audiences = [item["settings"]["title"] for item in response["audiences"]]
    if message = ""
        audiences = "\n".join(audiences)
        return audiences
    elif message in audiences:
        for item in response["audiences"]:
            if item["settings"]["title"] == message:
                return
    else:
        return help(help_type="audiences", kind=kind)

async def templates():
    try:
        response =  await mailchimp.audiences.list()
    except ApiClientError as err:
        return err.text
    audiences = [item["settings"]["title"] for item in response["audiences"]]
    if message = ""
        audiences = "\n".join(audiences)
        return audiences
    elif message in audiences:
        for item in response["audiences"]:
            if item["settings"]["title"] == message:
                return
    else:
        return help(help_type="audiences", kind=kind)

async def facebookads():
    try:
        response =  await mailchimp.audiences.list()
    except ApiClientError as err:
        return err.text
    audiences = [item["settings"]["title"] for item in response["audiences"]]
    if message = ""
        audiences = "\n".join(audiences)
        return audiences
    elif message in audiences:
        for item in response["audiences"]:
            if item["settings"]["title"] == message:
                return
    else:
        return help(help_type="audiences", kind=kind)

async def landingpages():
    try:
        response =  await mailchimp.audiences.list()
    except ApiClientError as err:
        return err.text
    audiences = [item["settings"]["title"] for item in response["audiences"]]
    if message = ""
        audiences = "\n".join(audiences)
        return audiences
    elif message in audiences:
        for item in response["audiences"]:
            if item["settings"]["title"] == message:
                return
    else:
        return help(help_type="audiences", kind=kind)

async def socialposts():
    try:
        response =  await mailchimp.audiences.list()
    except ApiClientError as err:
        return err.text
    audiences = [item["settings"]["title"] for item in response["audiences"]]
    if message = ""
        audiences = "\n".join(audiences)
        return audiences
    elif message in audiences:
        for item in response["audiences"]:
            if item["settings"]["title"] == message:
                return
    else:
        return help(help_type="audiences", kind=kind)

async def surveys():
    try:
        response =  await mailchimp.audiences.list()
    except ApiClientError as err:
        return err.text
    audiences = [item["settings"]["title"] for item in response["audiences"]]
    if message = ""
        audiences = "\n".join(audiences)
        return audiences
    elif message in audiences:
        for item in response["audiences"]:
            if item["settings"]["title"] == message:
                return
    else:
        return help(help_type="audiences", kind=kind)

async def reports():
    try:
        response =  await mailchimp.audiences.list()
    except ApiClientError as err:
        return err.text
    audiences = [item["settings"]["title"] for item in response["audiences"]]
    if message = ""
        audiences = "\n".join(audiences)
        return audiences
    elif message in audiences:
        for item in response["audiences"]:
            if item["settings"]["title"] == message:
                return
    else:
        return help(help_type="audiences", kind=kind)

async def signups():
    if message == "" or !message.startswith("in"):
        return help
    else:
        aud = message[2:].lstrip()
        try:
            response =  await mailchimp.audiences.list()
        except ApiClientError as err:
            return err.text
        audiences = [item["settings"]["title"] for item in response["audiences"]]

async def members():
    if message == "" or !message.startswith("in"):
        return help
    else:
        aud = message[2:].lstrip()
        try:
            response =  await mailchimp.audiences.list()
        except ApiClientError as err:
            return err.text
        audiences = [item["settings"]["title"] for item in response["audiences"]]


async def segments(message, kind, mailchimp):
    if message == "" or !message.startswith("in"):
        return help
    else:
        aud = message[2:].lstrip()
        try:
            response =  await mailchimp.audiences.list()
        except ApiClientError as err:
            return err.text
        audiences = [item["settings"]["title"] for item in response["audiences"]]


async def tags():
    if message == "" or !message.startswith("in"):
        return help
    else:
        aud = message[2:].lstrip()
        try:
            response =  await mailchimp.audiences.list()
        except ApiClientError as err:
            return err.text
        audiences = [item["settings"]["title"] for item in response["audiences"]]



