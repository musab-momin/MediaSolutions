from django.http.response import HttpResponse, StreamingHttpResponse
from django.shortcuts import redirect, render
from .models import Image
from .forms import ImageForm
from PIL import Image


# Create your views here.
def index(request):
    form = ImageForm()
    param = {'form': form}
    return render(request, 'index.htm', param)


def makechange(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)


        if form.is_valid():
            current_form = form.save()
            print('image is saved...!')
            changed_image = image_changer(current_form.image, current_form.desired_format)
            if changed_image is not None:
                path = changed_image;
                param = {'convertedImg': path}
                return render(request, 'download.htm', param)
            if current_form.desired_format == '.jpg':
                changed_image = image_changer(current_form.image, current_form.desired_format)
                if changed_image is not None:
                    path = changed_image;
                    param = {'convertedImg': path}
                    return render(request, 'download.htm', param)


            

    return HttpResponse('Something went wrong please try to visit again...')



def image_changer(img_name, format):
    print('function get called')
    print(format)
    l = str(img_name).split('.')
    temp = '.' + l[1]
    update_name = str(img_name).replace(temp, format)
    if format == '.jpg':
        user_img = Image.open(img_name)
        rgb = user_img.convert('RGB')
        user_img = rgb.save('C:/Users/User/DjangoProjects/MediaSol/convertor/media/'+update_name)
        return update_name
    user_img = Image.open(img_name)
    user_img = user_img.save('C:/Users/User/DjangoProjects/MediaSol/convertor/media/'+update_name)
    return update_name

