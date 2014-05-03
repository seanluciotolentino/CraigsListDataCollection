import time
import pickle
import urllib2
import json
import os

#parameters:
auth_token='b49d0f32cd93c0a3102d96bf7841c0c5'
start = int(time.time() - (48*60*60))
stop = int(time.time() - (24*60*60))
wdir = '/nfs/vinci/vinci.1/home/stolenti/CraigsListDataCollection'

#do a quick check to see if there's been updates to our lists
sources = ['categories','category_groups','locations']
additional = ['','','&level=metro']
dates = ["Tue, 10 Sep 2013 07:34:25 -0000", "Mon, 02 Sep 2013 07:34:25 -0000", "Mon, 02 Sep 2013 07:34:25 -0000"]
for i in range(len(sources)):
    last_update = os.popen("HEAD 'http://reference.3taps.com/{0}/?auth_token={1}{2}'".format(sources[i],auth_token,additional[i])).read().split("\n")[5][15:]
    assert last_update == dates[i],"update didn't match. Source:{0}, Updated{1}".format(sources[i],last_update)

#load locations and categories
locations = pickle.load(open(wdir+'/cl_locations','r'))
categories = pickle.load(open(wdir+'/cl_categories','r'))
category_groups = pickle.load(open(wdir+'/cl_category_groups'))
all_categories = categories+category_groups

#loop through categories and make a query for each
for category in all_categories:
    #make the api call and convert to python struct
    request = urllib2.Request("http://search.3taps.com/?auth_token=b49d0f32cd93c0a3102d96bf7841c0c5&category={0}&count=location.metro&timestamp={1}..{2}".format(category,start,stop))
    response = urllib2.urlopen(request)
    read = response.read()
    dictionary = json.loads(read)
    counts = {d["term"]:d["count"] for d in dictionary["counts"]}

    #open the file for this category and write to it
    f = open('{0}/data24-48/{1}.csv'.format(wdir,category),'a')  # 'a' for append
    f.write(time.ctime()+",")
    for location in locations:
        if location not in counts:
            f.write("0,")
        else:
            f.write("{0},".format(counts[location]))
    f.write('\n')
    f.close()

