import os
import constants as c

# Remove all empty directories from the FTP upload path
os.system ('find ' + c.cameraPath + ' -depth -type d -exec rmdir --ignore-fail-on-non-empty {} +')

# Remove all archive files past a threshold date
os.system ('find ' + c.archivePath + ' -mtime +' + str(c.archive_deletionThresholdDays) + ' -type d -exec rm -r {} +')
