import os

azureAccountName = os.environ.get('AZURE_ACCOUNT_NAME', 'cambackup')
azureAccountKey = os.environ.get('AZURE_ACCOUNT_KEY', '')

cameraPath = os.environ.get('CAMERA_PATH', '/home/ftpusers/camera/')
archivePath = os.environ.get('ARCHIVE_PATH', '/home/archive/camera/')

jpgContentType = "img/jpg"

alert_minThreshold = os.environ.get('ALERT_MIN_THRESHOLD', 50)
alert_maxThreshold = os.environ.get('ALERT_MAX_THRESHOLD', 1000)
filesize_minThreshold = os.environ.get('FILESIZE_MIN)_THRESHOLD', 10485)

notificationUrl = os.environ.get('NOTIFICATION_URL', '')

archive_deletionThresholdDays = os.environ.get('ARCHIVE_DELETION_THRESHOLD', 21)
