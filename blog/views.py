        
from django.shortcuts import render,HttpResponse,redirect

from . models import Files
# myuploadfile

def index(request):
    if request.method == "POST" :
        files = request.FILES.getlist("files")
        file_list = []
        
        for file in files:
            new_file=Files(file=file)
            new_file.save()
            file_list.append(new_file.file.url)
            
        # return render(request, 'index.html', {'new_urls': str(new_file.file.url)})
        return render(request, 'index.html', {'new_urls': file_list})
    else:
        return render (request, 'index.html')


        