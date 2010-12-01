
# To customize this app:
#   1. Replace phone number with your cell phone.
#   2. Replace Twitter ID ("tropohelp") with your Twitter ID

text = currentCall.initialText.lower()

# If someone tweets either a reply or a mention that includes the word "fail"
# send a text message to a cell phone to that the recipient can check out the
# tweet

if text.find("fail") > -1:
    message("Whoa! " + currentCall.callerID + " is tweeting a fail",   {"to":"tel:+14075551212", "network":"SMS"})
    
# Is the message a "reply", i.e. a message directly to the Twitter account?
# If so, check the message for different keywords and take actions.

# (The reason for not sending messages out in reply to a "mention" is that it
# may be harder to guess exactly what the person is looking for based purely on a 
# keyword.  With a message sent to the account (a "reply") you have a better 
# chance of replying with accurate info.

elif text.find("@tropohelp") == -1:  

    if text.find("help") > -1:
        say("Tropo lets you build apps that interact via voice, SMS, IM and Twitter. See http://www.tropo.com/ for more.")
        message("Tropo help request from: " + currentCall.callerID, {"to":"tel:+14075551212", "network":"SMS"})

    elif text.find("faq") > -1:
        say("The Tropo FAQ is at https://www.tropo.com/docs/scripting/faq.htm")

    elif text.find("documentation") > -1:
        say("Tropo docs are at https://www.tropo.com/docs/")


