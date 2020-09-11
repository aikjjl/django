from django.shortcuts import render

# Create your views here.


## 返回给用户页面bookadd.html
def addbook(request):
    return render(request, 'bookadd.html')


# 向图书馆增加数据GET或POST方法方法
def addbooktodatabase(request):
    # 获取参数book_name,author,author_age
    if request.method == "GET":
        book_name = request.GET["book_name"]
        author_name = request.GET["author"]
        author_age = request.GET["author_age"]
    else:
        book_name = request.POST["book_name"]
        author_name = request.POST["author"]
        author_age = request.POST["author_age"]

    ## 先增加作者信息
    from polls.models import Person
    person = Person()
    person.name = author_name
    person.age = author_age
    person.save()
    ## 增加图书信息
    from polls.models import Book
    bookadded = Book(name=book_name)
    # 保存修改
    bookadded.person_id = person.id
    bookadded.save()
    # 重定向到添加成功页面
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/addok/')


from django.shortcuts import render
def home(request):
    string="hahaha"
    lis=["a","b","c","d"]
    dic={'a':'哈哈','b':'多多'}
    lis1=map(str,range(100))
    return render(request, 'home.html',{'strin':string,'lis':lis,'dic':dic,'lis1':lis1})