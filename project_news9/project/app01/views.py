from django.shortcuts import render,redirect
from app01.models import NewsappNewsunit as news
from django.contrib.auth import authenticate
from django.contrib import auth
from datetime import datetime
import math

# Create your views here.
def index(request):
    return render(request,'index.html',locals())

def showall(request):
    items = news.objects.all()
    return render(request,'showall.html',locals())
def edit(request):
    if request.method=='POST':
        id = request.POST['id']
        recd = news.objects.get(id=id)
        recd.title = request.POST['title']
        recd.catego = request.POST['catego']
        recd.message = request.POST['message']
        recd.nickname = request.POST['nickname']
        recd.press = request.POST['press']
        try:
            recd.save()
            return redirect('/showall/')
        except:
            message01 = '修改資料發生錯誤'
            return render(request,'edit.html',locals())
            #return redirect('/showall/')
    elif request.method=='GET':
        myid = request.GET['id']
        items = news.objects.get(id=myid)
        id = items.id
        title = items.title
        catego = items.catego
        message = items.message
        nickname = items.nickname
        press = items.press
        return render(request,'edit.html',locals())
pagenum = 1    
def page1(request):
    global pagenum
    pagesize = 8
    #可以顯示的必須enabled=True
    items = news.objects.filter(enabled=True)
    #計算筆數兩種方法：(1).items.count()。(2)len(items)
    #totalnum = len(items)
    totalnum = items.count()
    #totalpagenum = totalnum//pagesize
    totalpagenum = math.ceil(totalnum/pagesize)

    #下一頁
    #若是由form傳來get變數：request.GET['pagebtn']
    #若是由網址?pagebtn=..傳來的get變數：request.GET.get('pagebtn')
    #網址傳來筆數，一律都是文字（就算是數字，也是文字）== '1'
    #由目前pagenum來計算相關顯示數據
    startnum = (pagenum-1)*pagesize
    endnum = pagenum*pagesize
    items = news.objects.filter(enabled=True).order_by('id')[startnum:endnum]
    #若是下一頁，上一頁，再修改所要顯示的數據
    if request.GET.get('pagebtn') == '1':
        if pagenum <= totalpagenum-1:
            pagenum += 1        
            startnum = (pagenum-1)*pagesize
            endnum = pagenum*pagesize
            items = news.objects.filter(enabled=True).order_by('id')[startnum:endnum]
    #上一頁
    elif request.GET.get('pagebtn') == '-1':
        if pagenum >= 2:
            pagenum -= 1        
            startnum = (pagenum-1)*pagesize
            endnum = pagenum*pagesize
            items = news.objects.filter(enabled=True).order_by('id')[startnum:endnum]
    '''
    elif request.GET.get('pagebtn') == None:
        pagenum = 1        
        startnum = 1
        endnum = pagesize
        items = news.objects.filter(enabled=True).order_by('id')[startnum:endnum]
        '''
    #把全域變數設定到local筆數
    currentpagenum = pagenum
    return render(request,'page1.html',locals())

def detail(request):
    id = request.GET.get('id')
    item = news.objects.filter(id=id)
    if len(item)>0:
        #注意：若用filter查詢，結果是個list陣列，第一筆資料為item[0]（get查詢不是list陣列）
        title = item[0].title
        catego = item[0].catego
        message = item[0].message
        nickname = item[0].nickname
        pubtime = item[0].pubtime
        pubtime = item[0].pubtime
    else:
        message01 = '找不到資料'
    return render(request,'detail.html',locals())

pagenum2 = 1    
def page2(request):
    global pagenum2
    pagesize = 8
    #可以顯示的必須enabled=True
    items = news.objects.filter(enabled=True).order_by('-id')
    #計算筆數兩種方法：(1).items.count()。(2)len(items)
    #totalnum = len(items)
    totalnum = items.count()
    #totalpagenum = totalnum//pagesize
    totalpagenum = math.ceil(totalnum/pagesize)

    #下一頁
    #若是由form傳來get變數：request.GET['pagebtn']
    #若是由網址?pagebtn=..傳來的get變數：request.GET.get('pagebtn')
    #網址傳來筆數，一律都是文字（就算是數字，也是文字）== '1'
    #由目前pagenum2來計算相關顯示數據
    startnum = (pagenum2-1)*pagesize
    endnum = pagenum2*pagesize
    items = news.objects.filter(enabled=True).order_by('-id')[startnum:endnum]
    #若是下一頁，上一頁，再修改所要顯示的數據
    if request.GET.get('pagebtn') == '1':
        if pagenum2 <= totalpagenum-1:
            pagenum2 += 1        
            startnum = (pagenum2-1)*pagesize
            endnum = pagenum2*pagesize
            items = news.objects.filter(enabled=True).order_by('-id')[startnum:endnum]
    #上一頁
    elif request.GET.get('pagebtn') == '-1':
        if pagenum2 >= 2:
            pagenum2 -= 1        
            startnum = (pagenum2-1)*pagesize
            endnum = pagenum2*pagesize
            items = news.objects.filter(enabled=True).order_by('-id')[startnum:endnum]
    #把全域變數設定到local筆數
    currentpagenum = pagenum2
    return render(request,'page2.html',locals())        

    
def detail2(request):
    id = request.GET.get('id')
    item = news.objects.filter(id=id)
    if len(item)>0:
        #注意：若用filter查詢，結果是個list陣列，第一筆資料為item[0]（get查詢不是list陣列）
        title = item[0].title
        catego = item[0].catego
        message = item[0].message
        nickname = item[0].nickname
        pubtime = item[0].pubtime
        pubtime = item[0].pubtime
    else:
        message01 = '找不到資料'
    return render(request,'detail2.html',locals())    

def login2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        message01 = username
        #驗證是否為會員
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                message01 = '已經成功登入'
                return redirect('/page_admin2/')            
            else:
                message01 = '帳號尚未被啟用'
        else:
            message01 = '沒有這個帳號，登入錯誤'
    return render(request,'login2.html',locals())

pagenum3=1
def page_admin2(request):
    pagesize = 8
    keyword = request.GET.get('keyword')
    pagenum3 = int(request.GET.get('pagenum3', 1))

    if keyword:
        items_all = news.objects.filter(title__icontains=keyword).order_by('-pubtime')
    else:
        items_all = news.objects.all().order_by('-pubtime')

    totalnum = items_all.count()
    totalpagenum = math.ceil(totalnum / pagesize)

    startnum = (pagenum3 - 1) * pagesize
    endnum = pagenum3 * pagesize

    items = items_all[startnum:endnum]

    return render(request, 'page_admin2.html', {'items': items, 'currentpagenum': pagenum3, 'totalpagenum': totalpagenum, 'keyword': keyword})


def page2(request):
    pagesize = 8
    keyword = request.GET.get('keyword')
    pagenum3 = int(request.GET.get('pagenum3', 1))

    if keyword:
        items_all = news.objects.filter(title__icontains=keyword).order_by('-pubtime')
    else:
        items_all = news.objects.all().order_by('-pubtime')

    totalnum = items_all.count()
    totalpagenum = math.ceil(totalnum / pagesize)

    startnum = (pagenum3 - 1) * pagesize
    endnum = pagenum3 * pagesize

    items = items_all[startnum:endnum]

    return render(request, 'page2.html', {'items': items, 'currentpagenum': pagenum3, 'totalpagenum': totalpagenum, 'keyword': keyword})










def logout2(request):
    auth.logout(request)
    return redirect('/page2/')

def edit2(request,id=None):    
    if id is not None:
        if request.method=='POST':
            recd = news.objects.get(id=id)
            recd.title = request.POST['title']
            #讀取select的option值，直接POST[name]
            recd.catego = request.POST['catego']
            recd.message = request.POST['message']
            #讀取textarea的值，直接POST[name]
            recd.nickname = request.POST['nickname']
            recd.press = request.POST['press']
            #讀取radiobutton，乃是讀取radio-name值（不是id），因為有兩個radio，所以只能靠radio-value來鑑別了
            #若radio-value = 'yes'，則設定recd.enabled = True
            yesno = request.POST['enabled']
            if yesno=='yes':
                recd.enabled = True
            else:
                recd.enabled = False
            try:
                recd.save()
                return redirect('/page_admin2/')
            except:
                message01 = '修改資料發生錯誤'
                return render(request,'edit2.html',locals())
        else:
            #取得所有的catego
            #消除重複資料語法：distinct()
           
      
            categos = news.objects.values('catego').distinct()
            #categos = news.objects.values_list('catego').distinct()
            items = news.objects.get(id=id)
            id = items.id
            title = items.title
            catego = items.catego
            message = items.message
            nickname = items.nickname
            press = items.press   
            enabled = items.enabled
            return render(request,'edit2.html',locals())            
    elif id is None:
        message01 = '沒有給定要顯示的id'
        #return redirect('/page_admin2/')
        return render(request,'edit2.html',locals())            


def del2(request,id=None):    
    if id is not None:
        recd = news.objects.get(id=id)
        try:
            recd.delete()
            return redirect('/page_admin2/')
        except:
            message01 = '刪除發生錯誤'
            return render(request,'page_admin2.html',locals())
    elif id is None:
        message01 = '沒有給定要刪除的id'
        return redirect('/page_admin2/')
        #return render(request,'page_admin2.html',locals())            


def add2(request):
    if request.method=='POST':
        title = request.POST['title']
        catego = request.POST['catego']
        message = request.POST['message']
        nickname = request.POST['nickname']
        press = 0
        yesno = request.POST['enabled']
        #讀取radiobutton，乃是讀取radio-name值（不是id），因為有兩個radio，所以只能靠radio-value來鑑別了
        #若radio-value = 'yes'，則設定recd.enabled = True
        if yesno=='yes':
            enabled = True
        else:
            enabled = False
        #pubtime欄位不可以為null，一定要給值 
        pubtime = datetime.now()
        recd = news.objects.create(title=title,catego=catego,message=message,nickname=nickname,press=press,enabled=enabled,pubtime=pubtime)
        try:
            recd.save()
            return redirect('/page_admin2/')
        except:
            message01 = '新增一筆資料發生錯誤'
            return render(request,'add2.html',locals())
    else:
        #message01 = '無法新增資料'
        categos = ['公告','更新','活動','其它']

        return render(request,'add2.html',locals())            