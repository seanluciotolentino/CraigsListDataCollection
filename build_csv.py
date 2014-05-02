
import pickle
import urllib2
import json

locations = pickle.load(open('cl_locations','r'))
categories = pickle.load(open('cl_categories','r'))
category_groups = pickle.load(open('cl_category_groups','r'))
for category in categories+category_groups:
    #open the file for this category and write to it
    f = open('data0-24/{0}.csv'.format(category),'w')  # 'w' for write
    f.write('time,')    
    #add the location as header (first time only)
    for location in locations:
        f.write("{0},".format(location))
    f.write('\n')

    f.close()
