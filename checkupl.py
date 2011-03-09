import os
import commands
from os.path import join, getsize
import flickrapi

user_id='53011016@N00'
api_key='71e59cab4ff9d8958d572cfaa485f4c1'
api_secret= 'e9c6e341cc04f991'

flickr = flickrapi.FlickrAPI(api_key,api_secret)
(token, frob) = flickr.get_token_part_one(perms='read')
if not token: raw_input("Press ENTER after you authorized this program")
flickr.get_token_part_two((token, frob))

jpg_count = 0
found_count = 0

for root, dirs, files in os.walk('.'):
    for fil in files:
        fil_orig = commands.getoutput('exiftool "' + root+'/'+fil + '" |grep "Date/Time Original"')
        if fil_orig.find('Time Original') == -1: continue
        # exif data found        
        fil_orig = fil_orig[fil_orig.find(':')+1:].strip().replace(':','-',2)
        photos = flickr.photos_search(user_id=user_id, per_page='10',min_taken_date=fil_orig,max_taken_date=fil_orig)
        if photos.find('photos').attrib['total'] != '0':
            print 'Found and removed from disk:',root+'/'+fil
            os.remove(root+'/'+fil)
            found_count +=1
        else:
            print 'Not Found:',root+'/'+fil
        jpg_count += 1

print 'found_count',found_count
print 'jpg_count',jpg_count
