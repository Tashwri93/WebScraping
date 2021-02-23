#!/usr/bin/env python3

from bs4 import BeautifulSoup       #Used to scrap infomation on hackernews
import requests                     #http requests to get website
import json                         #used to print in JSON format


url_request = 'https://news.ycombinator.com/'
req = requests.get(url_request)                 #Making the http request
content = req.text                              #getting the body

soup = BeautifulSoup(content, "html.parser")

#variables assign to collect html tags
posts= soup.select(".storylink")            #collecting Title and Href link
author = soup.select(".subtext")            #collecting authors
subtext = soup.select(".subtext")           #collecting points
rank = soup.select(".rank")                 #collecting ranks


def hackernews(posts, subtext):
    hackernews_info = []

    #Looping through the variables to collect html tags throughout content page
    for idx, item in enumerate(posts):
        title = posts[idx].getText()
        href = posts[idx].get('href', None)
        ranks = int(rank[idx].getText().replace('.', ''))

        authors = author[idx].select('.hnuser')
        if len(authors):
            newauthors = authors[0].getText()
            
        points = subtext[idx].select('.score')
        if len(points):
            vote = int(points[0].getText().replace(' points', ''))
            
        #Collect data and put into a dictionary    
        hackernews_info.append({"title": title, "uri": href, "author": newauthors,          
                                "points": vote, "rank": ranks,})
        #output will be in JSON format
        hackernews_info_json = json.dumps(hackernews_info, indent=4)
        
    return hackernews_info_json

print(hackernews(posts,subtext))


