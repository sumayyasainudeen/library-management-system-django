from django.contrib import admin

from LibraryApp.models import BookModel, CancelledBooksModel, CategoryModel, IssueRequestModel, IssuedBooksModel, MemberModel, PaymentModel, PenaltyModel, ReturnRequestModel1, SuggestionsModel

# Register your models here.
@admin.register(CategoryModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','category_name')

@admin.register(BookModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','name','author','image','description','publish_year','language','price','quantity','category')
    
@admin.register(MemberModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','address','phone','dob','image','user')

@admin.register(IssueRequestModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','member','book','status')

@admin.register(IssuedBooksModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','member','book','issue_date','expiry_date','status')

@admin.register(CancelledBooksModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','member','book','cancelled_date','status')

@admin.register(ReturnRequestModel1)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','member','book','issue_date','expiry_date','return_date','over_due','status')

@admin.register(PenaltyModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','member','book','issue_date','expiry_date','return_date','over_due','penalty','reason','total','status')

@admin.register(PaymentModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','member','book','issue_date','expiry_date','return_date','over_due','penalty','reason','total','status')

@admin.register(SuggestionsModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','member','topic','suggestion','date')

