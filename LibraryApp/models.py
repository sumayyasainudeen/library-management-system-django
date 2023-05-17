from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ValidationError



# Create your models here.
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=70)
    category_image= models.ImageField(upload_to="image/", null=True)

class BookModel(models.Model):
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=70)
    author=models.CharField(max_length=220)
    image= models.ImageField(upload_to="image/", null=True)
    description=models.CharField(max_length=220)
    publish_year=models.IntegerField()
    language=models.CharField(max_length=70)
    price=models.IntegerField()
    quantity=models.IntegerField()


class MemberModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=220)
    phone=models.IntegerField()
    dob=models.DateField()
    image= models.ImageField(upload_to="image/", null=True)

class IssueRequestModel(models.Model):
    member=models.ForeignKey(MemberModel,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=50)

class IssuedBooksModel(models.Model):
    member=models.ForeignKey(MemberModel,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE,null=True)
    issue_date=models.DateField(auto_now_add=True)
    expiry_date=models.DateField()
    status=models.CharField(max_length=50)

class CancelledBooksModel(models.Model):
    member=models.ForeignKey(MemberModel,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE,null=True)
    cancelled_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=50)

class ReturnRequestModel1(models.Model):
    member=models.ForeignKey(MemberModel,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE,null=True)
    issue_date=models.DateField()
    expiry_date=models.DateField()
    return_date=models.DateField(auto_now_add=True)
    over_due = models.IntegerField()
    status=models.CharField(max_length=50)

class PenaltyModel(models.Model):
    member=models.ForeignKey(MemberModel,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE,null=True)
    issue_date=models.DateField()
    expiry_date=models.DateField()
    return_date=models.DateField(auto_now_add=True)
    over_due = models.IntegerField()
    penalty = models.IntegerField()
    reason = models.CharField(max_length=50)
    total = models.IntegerField()
    status=models.CharField(max_length=50)

class PaymentModel(models.Model):
    member=models.ForeignKey(MemberModel,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE,null=True)
    issue_date=models.DateField()
    expiry_date=models.DateField()
    return_date=models.DateField(auto_now_add=True)
    over_due = models.IntegerField()
    penalty = models.IntegerField()
    reason = models.CharField(max_length=50)
    total = models.IntegerField()
    status=models.CharField(max_length=50)

class SuggestionsModel(models.Model):
    member=models.ForeignKey(MemberModel,on_delete=models.CASCADE,null=True)
    topic = models.CharField(max_length=50)
    suggestion = models.CharField(max_length=250)
    date=models.DateField(auto_now_add=True)
   
 


