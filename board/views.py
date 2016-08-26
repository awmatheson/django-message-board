from django.shortcuts import render
from django.utils import timezone
from .models import Message

# Create your views here.
def message_board(request):
	messages = Message.objects.filter(sent_date__lte=timezone.now()).order_by('sent_date')
	return render(request, 'board/message_board.html', {'messages': messages})