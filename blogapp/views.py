from django.shortcuts import render,redirect
from blogapp.forms import BlogForm
from blogapp.models import Blog

# Create your views here.

def blg(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = BlogForm()
    return render(request,'index.html',{'form':form})

def show(request):
    blogs = Blog.objects.all()
    return render(request,"show.html",{'blogs':blogs})

def edit(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,'edit.html',{'blog':blog})

def update(request,id):
    if request.method=='POST':
        print("jj")
        blog = Blog.objects.get(id=id)
        form = BlogForm(request.POST,instance=blog)
        print("out")
        if form.is_valid():
            print("in")
            form.save()
            print("inside")
            return redirect("/show")
    else:
        form=BlogForm(instance=blog)
    context={
        'blog':blog,

    }
    return render(request,'edit.html',context)

def destroy(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("/show")



