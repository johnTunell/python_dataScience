import magic
from os import listdir
import os
from os.path import isfile, join
mypath = '/tf_files/symbols/blood_drop_cross'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

file_to_remove = mypath + '\\' + onlyfiles[0]
removed_files = 0
print file_to_remove
for image in onlyfiles:
    print image
    image_type = magic.from_file(image)
    image_type = image_type[:3]
    print image_type
    if image_type == 'PNG':
        print "remove image " + image
        os.remove(mypath + '/' + image)
        removed_files += 1

print removed_files
