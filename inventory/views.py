from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import branch, product, Login,sample,employ,stock,Requests
from _datetime import date,time,datetime


def invento(request):
    name = request.session["username"]
    uname = request.session["uname"]
    context = {'s': name, 'p': uname}
    return render(request, 'index.html',context)

def bhome(request):
    if "username" in request.session:
        name = request.session["username"]
        context = {'s':name}

        return render(request, 'branchhome.html',context)

    else:
        context = {"log": "You are Logged Out"}
        return render(request, "branchlog.html",context)



def phome(request):
    if request.method == 'POST':
        name = request.POST.get("search")
        search = product.objects.all()
        context = {'s': search, 'n': name}
        template = loader.get_template("product.html")
        return HttpResponse(template.render(context, request))
    else:
        return render(request, 'product.html')

def smt(request):
    template = loader.get_template('smrtphn.html')
    sam = product.objects.all()
    context = {'s': sam}
    return HttpResponse(template.render(context, request))
def ele(request):
    template = loader.get_template('elec.html')
    sam = product.objects.all()
    context = {'s': sam}
    return HttpResponse(template.render(context, request))
def storage(request):
    template = loader.get_template('sdevice.html')
    sam = product.objects.all()
    context = {'s': sam}
    return HttpResponse(template.render(context, request))




def bpro(request):
    if request.method == 'POST':
        name = request.POST.get("search")
        search = product.objects.all()
        context = {'s': search, 'n': name}
        template = loader.get_template("bproducts.html")
        return HttpResponse(template.render(context, request))
    else:
        return render(request, 'bproducts.html')




def reg(request):
    if request.method == 'POST':
        type = request.POST.get("type")

        branch_id=request.POST.get('bid')
        b_name = request.POST.get('bname')
        b_add = request.POST.get('add')

        b_loc = request.POST.get('loc')
        b_phone = request.POST.get('phn')
        email = request.POST.get('email')
        password = request.POST.get('passw')

        if type == '1':
            log = Login()
            log.email = email
            log.password = password

            log.usertype = type
            log.save()
            bkreg = branch()
            bkreg.branch_id = branch_id
            bkreg.dateofreg = date.today()
            bkreg.b_name = b_name
            bkreg.b_add = b_add
            bkreg.b_loc = b_loc
            bkreg.b_phone = b_phone
            bkreg.email = email
            bkreg.password = password
            bkreg.login = log

            bkreg.save()
            return HttpResponse("<script>alert('Registration Done');window.location='../home';</script>")
        return HttpResponse('error')

    return render(request, 'contact.html')





def editp(request):
    prod = product.objects.get(id=1)
    prod.qua= 6
    prod.save()
    # context = {'pro': prod}
    template = loader.get_template("proedit.html")
    return HttpResponse(template.render(request))
def branchlog(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('passw')

        if (Login.objects.filter(email=username, password=password).exists()):

            logins = Login.objects.filter(email=username, password=password)

            for value in logins:

                usertype = value.usertype

                if usertype == 1:
                    out = branch.objects.get(login=value)
                    request.session['uname'] = out.email
                    request.session['userid'] = out.id
                    request.session['username'] = out.b_name
                    name = request.session["username"]
                    uname = request.session["uname"]
                    context = {'s': name, 'p': uname}
                    # bid = branch.objects.get(login=value)
                    # request.session['branchid'] = bid.branch_id
                    # request.session["usertype"] = usertype

                    return render(request, 'branchhome.html',context)
                elif usertype == 0:
                    # request.session["usertype"] = usertype
                    out = branch.objects.get(login=value)
                    request.session['uname'] = out.email
                    request.session['userid'] = out.id
                    request.session['username'] = out.b_name
                    uname = request.session["uname"]
                    name = request.session["username"]

                    context = {'s': name,'p': uname}
                    return render(request, 'index.html',context)
                else:
                    context = {"error": "You are Logged Out"}

                    return render(request, "branchlog.html", context)
        else:

            template = loader.get_template("branchlog.html")
            context = {"error": "Invalid Username or Password"}
            return HttpResponse(template.render(context, request))
    else:

        template = loader.get_template("branchlog.html")
        context = {}
        return HttpResponse(template.render(context, request))
def stok(request):
    if "username" in request.session:
        sam = product.objects.all()
        context = {'s': sam}
        template = loader.get_template('branchstock.html')
        return HttpResponse(template.render(context, request))




    else:
        return render(request,"branchlog.html")





def logout(request):
    if "username" in request.session:
        del request.session["username"]

    return render(request,"branchlog.html")




def sampl(request):
    if "userid" in request.session:
        name = request.session["userid"]
        # pro = product.objects.get(id)
        context = {'sam':name}
        return render(request,"rgh.html",context)

    else:
        return render(request, "branchlog.html")



# def display(request):
#     template = loader.get_template(")
#     sam = branch.objects.all()
#     context = {'s': sam}
#     return HttpResponse(template.render(context, request))

def emp(request):

    sam = branch.objects.all()
    context = {'s': sam}
    now = datetime.now()
    if request.method == 'POST':
        e = employ()
        e.name = request.POST.get('name')
        e.dateofjoin = date.today()
        e.timeofjoin = now.strftime("%I:%M:%S %p")
            # datetime.time(datetime.now())
        e.dob = request.POST.get('dob')

        e.gender = request.POST.get('gender')
        e.add = request.POST.get('address')
        e.town = request.POST.get('town')
        e.district = request.POST.get('dist')
        e.email = request.POST.get('mail')

        e.phn = request.POST.get('phn')
        e.out_id = request.POST.get('out')
        e.save()
        return HttpResponse("<script>alert('Registration Completed');window.location='../home';</script>")
    else:
        template = loader.get_template("edetails.html")
        return HttpResponse(template.render(context, request))

def view_emp(request):
        template = loader.get_template("viewemp.html")
        ed = employ.objects.all()
        o = branch.objects.all()
        context = {'s': ed, 'p': o}
        return HttpResponse(template.render(context, request))
def edit(request):
    now = datetime.now()
    if request.method == 'POST':
        name = request.POST.get("search")
        search = employ.objects.all()
        b = branch.objects.all()
        context = {'s': search, 'n': name,'p':b}
        template = loader.get_template("edite.html")
        return HttpResponse(template.render(context, request))

    else:
        return render(request, 'edite.html')
def e_emp(request,id):
    edit = employ.objects.get(id=id)
    return render(request,'e_dit.html',{'dist':edit})
def nxt(request,id):
    if request.method == 'POST':
        e = employ.objects.get(id=id)
        e.outlet = request.POST.get('out')
        e.name = request.POST.get('name')

        e.dob = request.POST.get('dob')

        e.gender = request.POST.get('gender')
        e.add = request.POST.get('address')
        e.town = request.POST.get('town')
        e.district = request.POST.get('dist')
        e.email = request.POST.get('mail')

        e.phn = request.POST.get('phn')
        e.save()
        return HttpResponse("<script>alert('Successfully Updated');window.location='../viewemp';</script>")
    else:
        e = employ.objects.get(id=id)
        return render(request, 'e_dit.html', {'dist': e})

def delEmp(request,id):
    dist = employ.objects.get(id=id)
    dist.delete()
    template = loader.get_template("viewemp.html")

    return HttpResponse("<script>alert('Deleted');window.location='../viewemp';</script>")

def pro(request):

    if request.method == 'POST':
        categ = request.POST.get('categ')

        pname = request.POST.get('pname')
        model = request.POST.get('model')
        company = request.POST.get('company')

        price = request.POST.get('price')

        s = stock()
        s.pname = pname
        s.save()
        pr = product()

        pr.categ = categ

        pr.p_name = pname
        pr.model_name = model
        pr.manfac = company
        pr.price=price
        pr.stk = s


        pr.save()

        return HttpResponse("<script>alert('Product Added');window.location='../product';</script>")
    else:
        return render(request,"proadd.html")


def stockview(request):
        template = loader.get_template("productsview.html")
        ed = product.objects.all()
        st = stock.objects.all()
        context = {'s': ed, 'p': st}
        return HttpResponse(template.render(context, request))
def addstk(request,id):
    if request.method == 'POST':
        e = stock.objects.get(id=id)
        e.pname = request.POST.get('pname')
        e.pro_id = request.POST.get('pid')

        e.qua = request.POST.get('qua')
        e.save()

        return HttpResponse("<script>alert('Stock Added');window.location='../admin_stockview';</script>")
    else:
        e = product.objects.get(id=id)
        return render(request, 'addstock.html', {'dist': e})

def reqst(request):
    template = loader.get_template("reqst.html")
    ed = product.objects.all()
    st = stock.objects.all()
    context = {'s': ed, 'p': st}
    return HttpResponse(template.render(context, request))


def rform(request,id):
    if "username" in request.session:
        name = request.session["username"]
        pro = product.objects.get(id=id)

        e = Requests()
        e.rdate = date.today()
        e.branch = name
        e.pname = pro.p_name
        e.model = pro.model_name
        e.brand = pro.manfac
        e.save()

        return HttpResponse("<script>alert('Request Sent');window.location='../req';</script>")
    else:
        return render(request, "branchlog.html")
def viewreq(request):
    template = loader.get_template('rform.html')
    sam = Requests.objects.all()
    context = {'s': sam}
    return HttpResponse(template.render(context, request))

def delrq(request,id):
    if "username" in request.session:
        dist = Requests.objects.get(id=id)
        dist.delete()
        return HttpResponse("<script>alert('Deleted');window.location='../reqstview';</script>")
    else:
        return render(request, "branchlog.html")
def proview(request):
    sam = product.objects.all()
    context = {'s': sam}
    template = loader.get_template('viewall.html')
    return HttpResponse(template.render(context, request))
def delp(request,id):
    if "username" in request.session:
        dist = product.objects.get(id=id)
        stk = stock.objects.get(id=id)
        dist.delete()
        stk.delete()
        return HttpResponse("<script>alert('Deleted');window.location='../viewpro';</script>")
    else:
        return render(request, "branchlog.html")
def branchall(request):
    sam = branch.objects.all()
    context = {'s': sam}
    template = loader.get_template('branchall.html')
    return HttpResponse(template.render(context, request))
def editb(request,id):
    if request.method == 'POST':
        e = branch.objects.get(id=id)
        e.b_name = request.POST.get('out')
        e.b_add = request.POST.get('add')

        e.b_loc = request.POST.get('loc')

        e.b_phone = request.POST.get('phn')

        e.email = request.POST.get('email')
        e.password = request.POST.get('pass')

        e.phn = request.POST.get('phn')
        e.save()
        return HttpResponse("<script>alert('Successfully Updated');window.location='../branchall';</script>")
    else:
        e = branch.objects.get(id=id)
        return render(request, 'branchedit.html', {'dist': e})
def delb(request,id):
    if "username" in request.session:
        dist = branch.objects.get(id=id)
        dq = Login.objects.get(id=id)
        e = employ.objects.get(out_id=id)
        dq.delete()
        e.delete()

        dist.delete()

        return HttpResponse("<script>alert('Deleted');window.location='../branchall';</script>")
    else:
        return render(request, "branchlog.html")
def change(request):
    if "userid" in request.session:
        uid = request.session["userid"]
        if request.method == 'POST':
            username = request.POST.get('email')
            password = request.POST.get('passw')

            if (Login.objects.filter(email=username, password=password).exists()):
                logins = Login.objects.get(id=uid)
                logins.password = request.POST.get('npassw')
                logins.save()
                return HttpResponse("<script>alert('Success');window.location='../login';</script>")
            else:
                context = {"error": "Invalid Username or Password"}
                return render(request, "changepass.html",context)

        else:
            return render(request, "changepass.html")
    else:
        context = {"log": "You are Logged Out"}
        return render(request, "changepass.html", context)





































