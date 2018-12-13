import os
import errno
import socket
import azure.storage
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import requests
import constants as c

def notify(alerttype, message):
	payload = { 'alerttype' : alerttype, 'message' : message }
	r = requests.post(c.notificationUrl, json = payload)
	return r

def toUnicodeOrBust(obj, encoding='utf-8'):
	if isinstance(obj, basestring):
		if not isinstance(obj, unicode):
			obj = unicode(obj, encoding)
	return obj

def walkFilesInDirectory(path):
	flatFiles = []
	for root, dirs, files in os.walk(path):
		for name in files:
			flatFiles.append([root, name])
			#print os.path.join(root, name)
	return flatFiles

def isConnected():
	try:
		# see if we can resolve the host name -- tells us if there is a DNS listening
		host = socket.gethostbyname("microsoft.com")
		print (host)
		# connect to the host -- tells us if the host is actually reachable
		s = socket.create_connection((host, 80), 2)
		return True
	except:
		 pass
	return False

def archiveFile(filepath, archivepath, filename):
	#print filepath + " : " + archivepath + " : " + filename
	if (not os.path.exists(archivepath)):
		os.makedirs(archivepath)
	os.rename(filepath, os.path.join(archivepath, filename))


def uploadToAzure(files):
	block_blob_service = BlockBlobService(account_name = c.azureAccountName, account_key = c.azureAccountKey)

	totalFiles = str(len(files))
	fileCount = 0

	for file in files:
		fileCount += 1
		print ("Processing: " + file[1] + " (" + str(fileCount) + "/" + totalFiles + ")")
		filepath = os.path.join(file[0], file[1])
		archivepath = file[0].replace(c.cameraPath, c.archivePath)

		#print cameraPath + " : " + archivePath + " : " + archivepath

		if (filepath[-4:] == ".jpg") and (os.path.getsize(filepath) > c.filesize_minThreshold):
			try:
				containerName = file[0][20:28]
				block_blob_service.create_container(containerName)
				block_blob_service.create_blob_from_path(
					container_name = containerName, 	# Extract the date
					blob_name = file[1],			# filename
					file_path = filepath,
					content_settings = ContentSettings(content_type = c.jpgContentType)
					)
				try:
					archiveFile(filepath, archivepath, file[1])
				except OSError as e:
					print (e.errno)
			except:
				pass
		else:
			print ("Incorrect extension or file size below minimum threshold. Archiving.")
			archiveFile(filepath, archivepath, file[1])

#
# Start Here
#

# Find the files we need to process
files = walkFilesInDirectory(c.cameraPath)
numfiles = len(files)

print ("Found " + str(numfiles) + " to process...")

if (numfiles < c.alert_minThreshold):
	print ("Too few record - Alert someone")
	notify('TooFewRecords', str(numfiles))

if (numfiles > c.alert_maxThreshold):
	print ("Too many files backing up - Alert someone")
	notify('TooManyRecords', str(numfiles))

uploadToAzure(files)

print ("success")

