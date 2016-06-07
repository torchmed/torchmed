from fabric.api import local

def makemessages():
	local('django-admin makemessages --all')

def compilemessages():
	local('django-admin compilemessages')

def resetdb():
	local('sudo rm -rf data/*')	