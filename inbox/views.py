from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from a_user.models import Profile
from .models import *
from .forms import *
# Create your views here.
@login_required
def inbox_view(request, conversation_id=None):
    conversation = Conversation.objects.first()
    my_conversations = Conversation.objects.filter(participants=request.user)
    if conversation_id:
        conversation = get_object_or_404(my_conversations,id=conversation_id)
    else:
        conversation = None
    context ={
        'conversation' : conversation,
        'my_conversations' : my_conversations
    }
    return render(request, 'inbox.html',context)





