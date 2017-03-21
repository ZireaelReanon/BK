from django.shortcuts import render
from .models import Room
def show_room(request):
	rooms=Room.objects.all()
	print (rooms)
	context={
		"rooms":rooms

	}
	return render(request,"main_menu.html",context)