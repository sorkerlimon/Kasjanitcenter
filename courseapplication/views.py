from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from .models import Course, CourseRegistration
from .forms import CourseRegistrationForm
from .models import Course
# Create your views here.

def index(request):
    return HttpResponse('dfsfs')


# def course_registration(request):
#     if request.method == 'POST':
#         form = CourseRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('registration_success')  # Redirect to a success page or another appropriate URL
#     else:
#         form = CourseRegistrationForm()
    
#     return render(request, 'index.html', {'form': form,  })


def course_registration(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        course_title = request.POST.get('course_title')
        # print(course_title)

        course_registration = CourseRegistration(
            name=request.POST.get('name'),
            father_name=request.POST.get('father_name'),
            mother_name=request.POST.get('mother_name'),
            national_id=request.POST.get('national_id'),
            address=request.POST.get('address'),
            mobile_number=request.POST.get('mobile_number'),
            bkash_transaction_id=request.POST.get('bkash_transaction_id'),
            payment_method=request.POST.get('payment_method'),
            advance=request.POST.get('advance'),
            image=request.FILES.get('image'),
        )
        
        course_registration.save()
        course_registration.courses = course_title
        course_registration.save()

        return redirect('registration_success')
    else:
        form = CourseRegistrationForm()
    
    return render(request, 'index.html', {'form': form, 'courses':courses})



def registration_success(request):
    return render(request, 'registration.html')
    # return HttpResponse('Successfully registered')

def error_404_view(request, exception):
    return render(request, 'error_404.html', status=404)