# Tropo "night service" app - answers IM, Twitter, Voice, SMS, while you aren't there.

# This app does not respond to any messages except during the specified timeframe.

# Time on Tropo servers is in UTC/GMT, so you need to adjust offset accordingly.
# US Eastern Daylight Savings Time is +4 hours, so 5pm is 17:00 EDT = 21:00 UTC

from datetime import *

if currentCall.initialText.find("@stratohelp") == -1:  # CHANGE TO YOUR TWITTER ID
    if datetime.now().hour not in range(12,21) :
        say("Our offices are currently closed. Please visit our web site at www.tropo.com")

# Uncomment these two lines if you want the app to take some action *during* office hours.
#    else:
#        say("Our offices are open. We'll reply back to you soon.")

