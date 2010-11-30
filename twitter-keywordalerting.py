
# To customize this app:
#   1. Replace phone number with your cell phone.
#   2. Replace Twitter ID ("tropohelp") with your Twitter ID

text = currentCall.initialText.lower()

if text.find("fail") > -1:
    message("Whoa! " + currentCall.callerID + " is tweeting a fail",   {"to":"tel:+14075551212", "network":"SMS"})
    
elif text.find("@tropohelp") == -1:   #Is it a reply?

    if text.find("help") > -1:
        say("Tropo lets you build apps that interact via voice, SMS, IM and Twitter. See http://www.tropo.com/ for more.")
        message("Tropo help request from: " + currentCall.callerID, {"to":"tel:+14075551212", "network":"SMS"})

    elif text.find("faq") > -1:
        say("The Tropo FAQ is at https://www.tropo.com/docs/scripting/faq.htm")

    elif text.find("documentation") > -1:
        say("Tropo docs are at https://www.tropo.com/docs/")


