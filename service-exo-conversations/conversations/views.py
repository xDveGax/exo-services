from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

import json


@login_required
def room(request, room_name):
    return render(request, 'conversation/chat.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
