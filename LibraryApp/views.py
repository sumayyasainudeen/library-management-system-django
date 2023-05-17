
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from datetime import timedelta, date
from LibraryApp.models import BookModel, CancelledBooksModel, CategoryModel, IssueRequestModel, IssuedBooksModel, MemberModel, PaymentModel, PenaltyModel, ReturnRequestModel1, SuggestionsModel
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User




# Create your views here.
def index(request):
   book=BookModel.objects.all().order_by('-id')
   category=CategoryModel.objects.all()
   return render(request,'index.html',{'book':book,'category':category})

def signin_page(request):
     return render(request,'signin.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_home_page')
            else:
                login(request, user)
                auth.login(request, user)
                # messages.success(request,' Welcome...'+ user.first_name)
                return redirect('index')
        else:
            messages.info(request,'Please Register First!')
            return redirect('signin_page')
    return redirect('signin_page')


def admin_home_page(request):
    return render(request,'admin/adminhome.html')

def add_category_page(request):
    return render(request,'admin/addcategory.html')

def add_category(request):
     if request.method == 'POST':
        cname = request.POST['categoryname']
        image = request.FILES.get('file')
        data = CategoryModel(category_name=cname,category_image=image)
        data.save()
        messages.success(request,'Category Added')
        return redirect('add_category_page')

def view_category(request):
    category = CategoryModel.objects.all()
    return render(request,'admin/showcategory.html',{'category':category})

def signout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('index')

def edit_category_page(request,pk):
    category = CategoryModel.objects.get(id=pk)
    return render(request,'admin/editcategory.html',{'category':category})

def edit_category(request,pk):
    if request.method == 'POST':
        category = CategoryModel.objects.get(id=pk)
        category.category_name= request.POST['categoryname']  

        old=category.category_image
        new=request.FILES.get('file')
        if old != None and new == None:
            category.category_image=old
        else:
            category.category_image=new

        category.save()
        return redirect ('view_category')

def delete_category(request,pk):
    category = CategoryModel.objects.get(id=pk)
    category.delete()
    return redirect('view_category')

def add_book_page(request):
    category=CategoryModel.objects.all()
    return render(request,'admin/addbook.html',{'category':category})

def add_book(request):
      if request.method == 'POST':
        select = request.POST['select']
        category = CategoryModel.objects.get(id=select)
        # cname=category.category_name
        name = request.POST['name']
        author = request.POST['author']
        image = request.FILES.get('file')
        desc = request.POST['description']
        year = request.POST['publishedyear']
        lang = request.POST['language']
        price = request.POST['price']
        qty = request.POST['quantity']
        
        data = BookModel(name=name,author=author,image=image,description=desc,publish_year=year,language=lang,price=price,quantity=qty,category=category)
        data.save()
        messages.success(request,'Book Added')
        return redirect('add_book_page')
      else:
        return redirect('add_book_page')

def view_books(request):
    books = BookModel.objects.all()
    return render(request,'admin/showbooks.html',{'books':books})

def edit_book_page(request,pk):
    book = BookModel.objects.get(id=pk)
    category=CategoryModel.objects.all()
    return render(request,'admin/editbook.html',{'book':book,'category':category})

def edit_book(request,pk):
    if request.method == 'POST':
        book = BookModel.objects.get(id=pk)
        book.name = request.POST['name']
        book.author = request.POST['author']
        book.description = request.POST['description']
        book.publish_year = request.POST['publishedyear']
        book.language = request.POST['language']
        book.price = request.POST['price']
        book.quantity = request.POST['quantity']
        select = request.POST['select']
        category = CategoryModel.objects.get(id=select)
        book.category = category

        old=book.image
        new=request.FILES.get('file')
        if old != None and new == None:
            book.image=old
        else:
            book.image=new

        book.save()
        return redirect ('view_books')
    else:
        return redirect('edit_book_page')

def delete_book(request,pk):
    book = BookModel.objects.get(id=pk)
    book.delete()
    return redirect('view_books')

def category_page(request,pk):
    cats= CategoryModel.objects.all()
    cat= CategoryModel.objects.get(id=pk)
    book= BookModel.objects.filter(category=cat).order_by('-id')
    return render(request,'category.html',{'book':book,'cat':cat,'cats':cats})

def book_detail(request,pk):
    book =BookModel.objects.filter(id=pk)
    return render(request,'bookdetails.html',{'book':book})

def more_books_page(request):
    books=BookModel.objects.all().order_by('-id')
    category=CategoryModel.objects.all()
    return render(request,'morebooks.html',{'books':books,'category':category})

def show_users(request):
    user = User.objects.all()
    member = MemberModel.objects.all()
    return render(request,'admin/showusers.html',{'member':member})

def delete_user(request,pk):
    member = MemberModel.objects.get(id=pk)
    member.delete()
    return redirect('show_users')


def signup_page(request):
    return render(request,'user/signup.html')



@login_required(login_url='signin_page')
def send_issue_request(request,pk):
    book =BookModel.objects.get(id=pk)
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    member = MemberModel.objects.get(user=current_user)
    data = IssueRequestModel(member=member,book=book,status='pending')
    data.save()
    return redirect('/')

def requested_books(request):
    current_user = request.user
    current_id = current_user.id
    member = MemberModel.objects.get(user=current_user)
    issue_requested_books = IssueRequestModel.objects.filter(member=member).order_by('-id')
    return render(request,'user/requestedbooks.html',{'books':issue_requested_books})

def issue_request_received(request):
    books = IssueRequestModel.objects.filter(status = 'pending').order_by('-id')
    return render(request,'admin/issuerequestreceived.html',{'books':books})

def issue_request_aproval(request,pk):
    book = IssueRequestModel.objects.get(id=pk)
    print(book.status)
    book.status='Issued'
    print(book.book.quantity)
    book.book.quantity=book.book.quantity-1
    print(book.book.quantity)
    book.save()
    book.book.save()

    ex_date = date.today() + timedelta(days=2)
    issued_book=IssuedBooksModel(member=book.member,book=book.book,expiry_date=ex_date,status='Issued')
    issued_book.save()
    book.delete()
    return redirect('issue_request_received')

def issued_books(request):
    current_user = request.user
    current_id = current_user.id
    member = MemberModel.objects.get(user=current_user)
    issued_books = IssuedBooksModel.objects.filter(member=member).order_by('-id')
    return render(request,'user/issuedbooks.html',{'books':issued_books})

def all_issued_books(request):
    issued_books = IssuedBooksModel.objects.all().order_by('-id')
    return render(request,'admin/viewissuedbooks.html',{'books':issued_books})

def issue_request_cancel(request,pk):
    book = IssueRequestModel.objects.get(id=pk)
    book.status='Cancelled'
    book.save()
    cancelled_book=CancelledBooksModel(member=book.member,book=book.book,status='Cancelled')
    cancelled_book.save()
    book.delete()
    return redirect('issue_request_received')

def cancelled_books(request):
    current_user = request.user
    current_id = current_user.id
    member = MemberModel.objects.get(user=current_user)
    cancelled_books = CancelledBooksModel.objects.filter(member=member).order_by('-id')
    return render(request,'user/cancelledbooks.html',{'books':cancelled_books})

def all_cancelled_books(request):
    books = CancelledBooksModel.objects.all().order_by('-id')
    return render(request,'admin/viewcancelledbooks.html',{'books':books})

def user_return_request_page(request):
    current_user = request.user
    current_id = current_user.id
    member = MemberModel.objects.get(user=current_user)
    books = IssuedBooksModel.objects.filter(member=member).order_by('-id')
    return render(request,'user/returnrequest.html',{'books':books})

def return_request(request,pk):
    book =IssuedBooksModel.objects.get(id=pk)
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    member = MemberModel.objects.get(user=current_user)
    issue_date=book.issue_date
    exp_date=book.expiry_date
    return_date=date.today()
    delta = return_date-issue_date
    days=delta.days
    if(days>2):
        extra_days=days-2
        over_due=extra_days*5
        data = ReturnRequestModel1(member=member,book=book.book,issue_date=issue_date,expiry_date=exp_date,over_due=over_due,status='pending')
        data.save()
        book.delete()
        return redirect('user_return_request_page')
    else:
        over_due=0
        data = ReturnRequestModel1(member=member,book=book.book,issue_date=issue_date,expiry_date=exp_date,over_due=over_due,status='pending')
        data.save()
        book.delete()
        return redirect('user_return_request_page')

def return_request_received(request):
    books = ReturnRequestModel1.objects.all().order_by('-id')
    return render(request,'admin/returnrequestreceived.html',{'books':books})

def add_penalty_form(request,pk):
    data = ReturnRequestModel1.objects.get(id=pk)
    return render(request,'admin/addpenalty.html',{'data':data})

def add_penalty(request,pk):
    if request.method == 'POST':
        penalty = request.POST['penalty']
        reason = request.POST['select']
        data = ReturnRequestModel1.objects.get(id=pk)
        total = data.over_due + int(penalty)
        penalty_data=PenaltyModel(member=data.member,
                                   book=data.book,
                                   issue_date=data.issue_date,
                                   expiry_date=data.expiry_date,
                                   return_date=data.return_date,
                                   over_due=data.over_due,
                                   penalty=penalty,
                                   reason=reason,
                                   total=total,
                                   status='pending')
        penalty_data.save()
        
        return redirect('return_request_received')
    else:
        return redirect('return_request_received')

def no_penalties(request,pk):
    penalty = 0
    reason = 'Nill'
    data = ReturnRequestModel1.objects.get(id=pk)
    data.book.quantity=data.book.quantity+1
    total = data.over_due 
    penalty_data=PenaltyModel(member=data.member,
                                   book=data.book,
                                   issue_date=data.issue_date,
                                   expiry_date=data.expiry_date,
                                   return_date=data.return_date,
                                   over_due=data.over_due,
                                   penalty=penalty,
                                   reason=reason,
                                   total=total,
                                   status='pending')
    penalty_data.save()
    data.book.save()   
    return redirect('return_request_received')
   

def return_request_aproval(request,pk):
    data = PenaltyModel.objects.all().order_by('-id')
    return render(request,'admin/viewpenalty.html',{'data':data})

def payment_details(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    member = MemberModel.objects.get(user=current_user)
    data = PenaltyModel.objects.filter(member=member).order_by('-id')
    return render(request,'user/payments.html',{'data':data})

def user_pay(request,pk):
    data = PenaltyModel.objects.get(id=pk)
    data.status='paid'
    data.book.quantity=data.book.quantity+1
    data.save()
    data.book.save()
    payment = PaymentModel(member=data.member,
                                   book=data.book,
                                   issue_date=data.issue_date,
                                   expiry_date=data.expiry_date,
                                   return_date=data.return_date,
                                   over_due=data.over_due,
                                   penalty=data.penalty,
                                   reason=data.reason,
                                   total=data.total,
                                   status='paid')
    payment.save()
    data.delete()
    return redirect('payment_details')

def view_payment(request):
    data = PaymentModel.objects.all()
    return render(request,'admin/viewpayments.html',{'data':data})

def payment_history(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    member = MemberModel.objects.get(user=current_user)
    data = PaymentModel.objects.filter(member=member).order_by('-id')
    return render(request,'user/paymenthistory.html',{'data':data})

def search_book(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        book = BookModel.objects.filter(name__icontains=search_term) 
        return render(request, 'user/viewsearch.html', {'book' : book })    

def view_profile(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    member = MemberModel.objects.get(user=current_user)
    return render(request,'user/viewprofile.html',{'user':user,'member':member})

def edit_profile(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    member = MemberModel.objects.get(user=current_user)
    return render(request,'user/editprofile.html',{'user':user,'member':member})

def profile_edit(request,pk):
    if request.method == 'POST':
        member = MemberModel.objects.get(id=pk)
        member.address= request.POST['address']  
        member.phone= request.POST['phonenumber']
        member.dob= request.POST['dob']

        old=member.image
        new=request.FILES.get('file')
        if old != None and new == None:
            member.image=old
        else:
            member.image=new

        member.save()
        return redirect('view_profile')
    
def suggestion_form(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    member = MemberModel.objects.get(user=current_user)
    return render(request,'user/suggestionform.html',{'user':user,'member':member})

def  suggestion_add(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    member = MemberModel.objects.get(user=current_user)
    if request.method == 'POST':
        topic= request.POST['topic']  
        suggestion= request.POST['suggestion']
        data = SuggestionsModel(member=member,topic=topic,suggestion=suggestion)
        data.save()
        return redirect('/')
    else:
        return redirect('suggestion_form')

def show_suggestions(request):
    data = SuggestionsModel.objects.all().order_by('-id')
    return render(request,'admin/usersuggestions.html',{'data':data})

    


def create_user(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        add = request.POST['address']
        email = request.POST['email']
        ph = request.POST['phonenumber']
        dob = request.POST['dob']
        # uname = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        image = request.FILES.get('file')

      

        # if User.objects.filter(username=uname).exists():
        #         messages.info(request,'This Username Already Exists!')
        #         return redirect('signup_page')
        if (password == cpassword):
            
                if User.objects.filter(email=email).exists():
                    messages.info(request,'This Email Already Exists!')
                    return redirect('signup_page')
                else:
                    user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=email,password=password)
                    user.save()

                    # random password generation
                    # password = User.objects.make_random_password()
                    # user.set_password(password)
                    # user.save(update_fields=['password'])

                    data = User.objects.get(id=user.id)
                    member = MemberModel(address=add,phone=ph,dob=dob,image=image,user=data)
                    member.save()
                    subject = 'Welcome To Public Library'
                    message = 'Dear member,\n Here Is Your Login Credentials,\n Username :'+ email +'\nPassword: '+ password
                    recipient =request.POST["email"]
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
                    return redirect('signin_page')
            
        else:
            messages.info(request,'Passwords should match!')
            return redirect('signup_page')
   
    else:
        return redirect('signup_page')


    
    

















# def create_user(request):
#     if request.method == 'POST':
#         fname = request.POST['firstname']
#         lname = request.POST['lastname']
#         add = request.POST['address']
#         email = request.POST['email']
#         ph = request.POST['phonenumber']
#         dob = request.POST['dob']
#         uname = request.POST['username']
#         password = request.POST['password']
#         image = request.FILES.get('file')

      
#         if User.objects.filter(username=uname).exists():
#             messages.info(request,'This Username Already Exists!')
#             return redirect('signup_page')
#         elif (fname[0].isupper()):
#             if len(ph) <= 10:
#                 if User.objects.filter(email=email).exists():
#                     messages.info(request,'This Email Already Exists!')
#                     return redirect('signup_page')
#                 else:
#                     user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=password)
#                     user.save()

#                     data = User.objects.get(id=user.id)
#                     member = MemberModel(address=add,phone=ph,dob=dob,image=image,user=data)
#                     member.save()
#                     messages.success(request,' Welcome...'+ data.first_name)
#                     return redirect('index')
#             else:
#                 messages.info(request,'Not a Valid Phone Number Number!')
#                 return redirect('signup_page')
#         else:
#             messages.info(request,'The First Letter of Firstname Should Be in UpperCase!')
#             return redirect('signup_page')

        
#     else:
#         return redirect('signup_page')

        
        
   
