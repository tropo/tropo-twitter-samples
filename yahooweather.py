#------------------------------------------
# Sample Tropo.com multi-channel weather app, specifically optimized for Twitter
#
# Copyright (c) 2010 Voxeo Corp.
# Created by Dan York
# See the LICENSE file for distribution and usage
#
# This is a variation of the sample app found at:
#
# http://github.com/voxeo/tropo-samples/blob/master/python/yahooweather.py
#
#------------------------------------------

import urllib2
from xml.dom import minidom, Node

answer()

if currentCall.channel == "VOICE":
    say( "Welcome to the Tropo dot com sample Yahoo weather app." )
    result = ask( "Please say the ZIP code for a weather check", { 'choices' : "[5 DIGITS]" })
    value = result.value
else:
    value = currentCall.initialText

text = value.lower()

if text.find("help") > -1:
    log("********** => Got a HELP REQUEST <== *************")
    say("Enter a 5-digit US ZIP code to receive the most recent weather report for that area.")
    message("Weather help request from: " + currentCall.callerID, {"to":"tel:+14079678424", "network":"SMS"})

elif text.find("fail") > -1:
    log("********** => Got a FAIL MESSAGE <== *************")
    message("Whoa! " + currentCall.callerID + " is tweeting a fail",   {"to":"tel:+14079678424", "network":"SMS"})

else:
  try:
    log( "zipCode <" + value + ">" )
    urlRead = urllib2.urlopen('http://weather.yahooapis.com/forecastrss?p=' + value + '&u=f')
    if urlRead :
        xml = minidom.parse( urlRead )
        if xml :
            for node in xml.documentElement.childNodes :
                if node.nodeName == "channel" :
                    for item_node in node.childNodes :
                        if item_node.nodeName == "item" :
                            item = ""
                            for weatherItem_node in item_node.childNodes:
                                if weatherItem_node.nodeName == "title" :
                                    weatherTitle = ""
                                    for weatherText_node in weatherItem_node.childNodes :
                                        weatherTitle += weatherText_node.nodeValue
                                if weatherItem_node.nodeName == "yweather:condition" :
                                    weatherTemp = weatherItem_node.getAttribute( 'temp' )
                                    weatherCondition = weatherItem_node.getAttribute( 'text' )
                                    if len( weatherTitle ) > 0 :
                                        say( weatherTitle + ": " + weatherTemp + " degrees Fahrenheit. " + weatherCondition)

  except:
    log( "Error getting XML")
    say("I am sorry, an error occurred while fetching the weather. Please enter a US ZIP code.")

if currentCall.channel == "VOICE":
    say( "Thats all. Goodbye!" )

hangup()

