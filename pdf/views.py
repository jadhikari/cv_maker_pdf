# views.py
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pdf/profile_created')  # Redirect to a success page or any other URL
    else:
        form = ProfileForm()
    return render(request, 'pdf/create_profile.html', {'form': form})


def resume(request, id):
    # Get the user profile or return a 404 error if not found
    user_profile = get_object_or_404(Profile, pk=id)
    
    # Load the template
    template = loader.get_template('pdf/cv.html')
    
    # Render the template with user_profile data
    html = template.render({'user_profile': user_profile})
    
    # Define PDF options
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }

    # Convert HTML to PDF
    pdf = pdfkit.from_string(html, False, options)

    # Prepare HTTP response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    
    return response


def list(request):
    profiles  = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})