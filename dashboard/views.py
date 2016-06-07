from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from users.models import User
# from files.models import File

# Create your views here.
# @login_required
def index(request):
	
	# user_files = File.objects.filter(user=request.user).order_by('-id')
	user_files = {}
	return render(request, 'dashboard.html', {'user_files':user_files})