#!/usr/bin/env python3.5
import csv, time, urllib.request, datetime

def royalsGame():
    with open('/home/jbg/.scripts/kcRoyals/schedule_2019.csv', 'r') as f:
        today = datetime.datetime.now()
        tomorrow = today + datetime.timedelta(days=1)
        tomorrow = datetime.datetime.strftime(tomorrow, "%m/%d/%y")
        today = datetime.datetime.strftime(today, "%m/%d/%y")
        reader = csv.DictReader(f)
        for row in reader:
            if today == row['START DATE']:
                game = row['SUBJECT'] + " @ " + row['START TIME ET']
                if row['LOCATION'] == 'Kauffman Stadium - Kansas City':
                    hw = 'Home'
                else:
                    hw = "Away: " + row['LOCATION']
                return push(game, hw)
            elif tomorrow == row['START DATE']:
                title = "No game today"
                message = "Next game is tomorrow, " + row["SUBJECT"]
                return push(title, message)
    return push("No Game Today" , "No game tomorrow either")

def push(title, message):
    token = 'adgw5hijy2noceynz1ummjy7vxjb8c'
    user_key = 'KskmehPrjtgoEixcUlF3zspzNaPXU7'
    post_data = 'token='+token+'&user='+user_key+'&title='+title+'&message='\
                +message+"&sound=classical"
    post_data = str.encode(post_data)
    push_url = 'https://api.pushover.net/1/messages.json'
    pushover = urllib.request.urlopen(push_url, data=post_data)
    return pushover
    
royalsGame()
