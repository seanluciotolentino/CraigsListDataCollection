A brief explanation of files and uses:

1. cl_locations -- a pickled python list of 3taps locations. They are "metro" areas. What these areas mean is here:

http://reference.3taps.com/locations/?auth_token=b49d0f32cd93c0a3102d96bf7841c0c5&level=metro
 
2. cl_categories -- a pickled python list of 3taps categories. What these mean is here:

http://reference.3taps.com/categories/?auth_token=b49d0f32cd93c0a3102d96bf7841c0c5

3. cl_category_groups -- a pickled list of 3taps category_groups

4. build_ref_list.py -- a python script to build the above three structures

5. build_csv.py -- a python script to initialize the headers of the csv files

6. update0-24.py -- a script that adds a row to each category data set. The row represents the number of craigslists postings for that category for each of metro area between 0 and 24 hours ago.

7. update24-48.py -- Same as above but with posting between 24 and 48 hours ago. 

8. cron_craigslist -- the cron job specification. Submitted with crontab cron_craigslist. Remove the cronjob with crontab -r and list the cronjobs with crontab -l

To do create a zip file, run the following command from the data directory

zip craigslist.zip ./craigslist_csv/*.csv

