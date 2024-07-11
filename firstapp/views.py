from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        f=Regist.objects.all()
        r=[]
        for i in f:
            r.append(i.dEmailId)
        if email in r:
            d="User already exist"
            return render(request,'signup.html',{'d':d})
        else:
            ob=Regist()
            ob.dEmailId=email
            ob.dbasePassword=password
            ob.save()
            request.session['email']=email
            print(email)
            return redirect('totalcaloriescalculating')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        backemail=request.POST.get('email')
        backpassword=request.POST.get('password')
        f=Regist.objects.get(dEmailId=backemail)
        if f.dbasePassword==backpassword:
             request.session['email']=backemail
             return redirect('homepage',id=1)
        else:
            e="Incorrect password"
            return render(request,'login.html',{'e':e})
    return render(request,'login.html')

def forgetpassword(request):
    if request.method=='POST':
        forgetemail=request.POST.get('forgetemail')
        newpassword=request.POST.get('newpassword')
        f=Regist.objects.all()
        r=[]
        for i in f:
            r.append(i.dEmailId)
        if forgetemail in r:
            already=Regist.objects.all().get(dEmailId=forgetemail)
            already.dbasePassword=newpassword
            already.save()
            messages.success(request,"Password reset successfully")
            return redirect('login')
        else:
            popup="Mail id does not exist"
            return render(request,'forgetpassword.html',{'popup':popup})
    return render(request,'forgetpassword.html')

def totalcaloriescalculating(request):
    if request.method=='POST':
        mailid=request.POST.get('mailid')
        age=int(request.POST.get('age'))
        weight=int(request.POST.get('weight'))
        height=int(request.POST.get('height'))
        if request.session['email']==mailid:
            finalcalories=(10 * weight) + (6.25 * height) - (5 * age ) + 5
            ob=caloriestarget()
            ob.Emailid=mailid
            ob.Age=age
            ob.Weight=weight
            ob.Height=height
            ob.Target=finalcalories
            ob.save()
            id = 1  
            return redirect('homepage', id=id)
        else:
            Error="Wrong Email you have entered"
            return render(request,'totalcaloriescalculating.html',{'Error':Error})
    return render(request,'totalcaloriescalculating.html')




def dater(request):
    id=1
    return redirect('homepage',id=id)

def dater2(request):
    id=2
    return redirect('homepage',id=id)

def dater3(request):
    id=3
    return redirect('homepage',id=id)
    
def homepage(request,id):
    import datetime
    x = datetime.datetime.now()
    if id==1:
        dataa = x.strftime("%Y-%m-%d")

    elif id==2:
        yesterday = x - datetime.timedelta(days=1)
        dataa = yesterday.strftime("%Y-%m-%d")
    elif id==3:
        tomorrow = x + datetime.timedelta(days=1)
        dataa = tomorrow.strftime("%Y-%m-%d")
    if request.session['email']:
            data=caloriestarget.objects.all().get(Emailid=request.session['email'])
            h=totalcalories.objects.all().filter(Emailid=request.session['email'],date=dataa)
            l=0
            p=0
            c=0
            f=0
            for i in h:
                l=l+i.totalcalories
            for j in h:
                p=p+j.totalprotein
            for k in h:
                c=c+k.totalcarbohydrate
            for g in h:
                f=f+g.totalfat
            context={
            'session':request.session['email'],
            'cal':data.Target,
            'totalc':l,
            'totalprotein':p,
            'totalcarbohydrate':c,
            'totalfat':f,
        }
            return render(request,'homepage.html',context)

def caloriestracker(request):
    breakfast=Breakfast.objects.all()
    lunch=Lunch.objects.all()
    dinner=Dinner.objects.all()
    context={
            "bk":breakfast,
            "lk":lunch,
            "dk":dinner
        }
    return render(request,'caloriestracker.html',context)







def addmeals(request):
    import datetime
    x = datetime.datetime.now()
    pdate = x.strftime("%Y-%m-%d")
    if request.method == 'POST':
        breakfast=request.POST.get('breakfast')
        quantity=request.POST.get('quantity')
        b=Breakfast.objects.get(id=breakfast)
    
        p=totalcalories()
        p.Emailid=request.session['email']
        p.date=pdate
        p.eatenfoods=b.breakfastfood
        p.totalcalories=int(quantity)*b.breakfastcalories
        p.totalprotein=int(quantity)*b.breakfastprotein
        p.totalcarbohydrate=int(quantity)*b.breakfastcarbohydrate
        p.totalfat=int(quantity)*b.breakfastfat

        p.save()
        return redirect('caloriestracker')

def addmeals2(request):
    import datetime
    x = datetime.datetime.now()
    qdate = x.strftime("%Y-%m-%d")
    if request.method == 'POST':
        lunch=request.POST.get('lunch')
        quantity2=request.POST.get('quantity2')
        c=Lunch.objects.get(id=lunch)

        q=totalcalories()
        q.Emailid=request.session['email']
        q.date=qdate
        q.eatenfoods=c.lunchfood
        q.totalcalories=int(quantity2)*c.lunchcalories
        q.totalprotein=int(quantity2)*c.lunchprotein
        q.totalcarbohydrate=int(quantity2)*c.lunchcarbohydrate
        q.totalfat=int(quantity2)*c.lunchfat

        q.save()
        return redirect('caloriestracker')

def addmeals3(request):
    import datetime
    x = datetime.datetime.now()
    rdate = x.strftime("%Y-%m-%d")
    if request.method == 'POST':
        dinner=request.POST.get('dinner')
        quantity3=request.POST.get('quantity3')
        d=Dinner.objects.get(dinnerfood=dinner)


        r=totalcalories()
        r.Emailid=request.session['email']
        r.date=rdate
        r.eatenfoods=d.dinnerfood
        r.totalcalories=int(quantity3)*d.dinnercalories
        r.totalprotein=int(quantity3)*d.dinnerprotein
        r.totalcarbohydrate=int(quantity3)*d.dinnercarbohydrate
        r.totalfat=int(quantity3)*d.dinnerfat

        r.save()
        return redirect('caloriestracker')
    
