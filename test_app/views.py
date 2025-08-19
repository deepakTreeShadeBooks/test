
from django.shortcuts import render, redirect
from .forms import ParagraphForm
from .models import Paragraph

def paragraph_form_view(request):
	messages = Paragraph.objects.order_by('-created_at')
	if request.method == 'POST':
		form = ParagraphForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'form.html', {'form': ParagraphForm(), 'success': True, 'messages': messages})
	else:
		form = ParagraphForm()
	return render(request, 'form.html', {'form': form, 'messages': messages})
