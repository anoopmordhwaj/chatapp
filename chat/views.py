from django.shortcuts import render, redirect
from chat.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def HomeView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room = request.POST.get('room')

        try:
            existing_room = Room.objects.get (room_name__icontains = room)

        except Room.DoesNotExist:
            r = Room.objects.create(room_name = room)
            r.save()
        return redirect("room", room_name = room, username = username)

    return render(request, 'home.html')



@login_required(login_url='/login/')
def RoomView(request, room_name, username):
    existing_room = Room.objects.get(room_name__icontains = room_name)
    get_messsage = Message.objects.filter(room = existing_room)

    recent_data = Recents.objects.filter(user_name = request.user).values().all()
        
    # This is for checking and updating Recent chats
    if not Recents.objects.filter(room_name = existing_room.room_name):
        r = Recents()
        r.user_name = request.user
        r.room_name = existing_room.room_name
        r.join_name  = username
        r.save()


    dist_recents = Recents.objects.filter(user_name = request.user).values().distinct()
    
    context = {
        'messages': get_messsage,
        'user' : username,
        'room_name' : existing_room.room_name,
        'recent_data' : dist_recents
        # 'pic': profile 
    }
    return render(request, 'room.html', context)