
from django.shortcuts import render, redirect
from .forms import ParagraphForm

def paragraph_form_view(request):
	if request.method == 'POST':
		form = ParagraphForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'form.html', {'form': ParagraphForm(), 'success': True})
	else:
		form = ParagraphForm()
	return render(request, 'form.html', {'form': form})
