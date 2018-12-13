import os
import constants as c

# Remove all empty directories from the FTP upload path
os.system ('find ' + c.cameraPath + ' -empty -type d -delete')

# Remove all archive files past a threshold date
os.system ('find ' + c.archivePath + ' -mtime +' + str(c.archive_deletionThresholdDays) + ' -delete')
