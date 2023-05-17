from LibraryApp import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('signin_page',views.signin_page,name='signin_page'),
    path('signin',views.signin,name='signin'),
    path('admin_home_page',views.admin_home_page,name='admin_home_page'),
    path('signout',views.signout,name='signout'),

    path('add_category_page',views.add_category_page,name='add_category_page'),
    path('add_category',views.add_category,name='add_category'),
    path('view_category',views.view_category,name='view_category'),
    path('edit_category_page/<int:pk>',views.edit_category_page,name='edit_category_page'),
    path('edit_category/<int:pk>',views.edit_category,name='edit_category'),
    path('delete_category/<int:pk>',views.delete_category,name='delete_category'),

    path('add_book_page',views.add_book_page,name='add_book_page'),
    path('add_book',views.add_book,name='add_book'),
    path('view_books',views.view_books,name='view_books'),
    path('edit_book_page/<int:pk>',views.edit_book_page,name='edit_book_page'),
    path('edit_book/<int:pk>',views.edit_book,name='edit_book'),
    path('delete_book/<int:pk>',views.delete_book,name='delete_book'),

    path('category_page/<int:pk>',views.category_page,name='category_page'),
    path('book_detail/<int:pk>',views.book_detail,name='book_detail'),
    path('more_books_page',views.more_books_page,name='more_books_page'),

    path('signup_page',views.signup_page,name='signup_page'),
    path('create_user',views.create_user,name='create_user'),

    path('send_issue_request/<int:pk>',views.send_issue_request,name='send_issue_request'),
    path('requested_books',views.requested_books,name='requested_books'),

    path('show_users',views.show_users,name='show_users'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user'),

    path('issue_request_received',views.issue_request_received,name='issue_request_received'),
    path('issue_request_aproval/<int:pk>',views.issue_request_aproval,name='issue_request_aproval'),
    path('issue_request_cancel/<int:pk>',views.issue_request_cancel,name='issue_request_cancel'),
    path('issued_books',views.issued_books,name='issued_books'),
    path('cancelled_books',views.cancelled_books,name='cancelled_books'),
    path('all_issued_books',views.all_issued_books,name='all_issued_books'),
    path('all_cancelled_books',views.all_cancelled_books,name='all_cancelled_books'),

    path('user_return_request_page',views.user_return_request_page,name='user_return_request_page'),
    path('return_request/<int:pk>',views.return_request,name='return_request'),
    path('return_request_received',views.return_request_received,name='return_request_received'),
    path('add_penalty_form/<int:pk>',views.add_penalty_form,name='add_penalty_form'),
    path('add_penalty/<int:pk>',views.add_penalty,name='add_penalty'),
    path('no_penalties/<int:pk>',views.no_penalties,name='no_penalties'),
    path('return_request_aproval/<int:pk>',views.return_request_aproval,name='return_request_aproval'),
    path('payment_details',views.payment_details,name='payment_details'),
    path('user_pay/<int:pk>',views.user_pay,name='user_pay'),
    path('view_payment',views.view_payment,name='view_payment'),
    path('payment_history',views.payment_history,name='payment_history'),
    path('search_book',views.search_book,name='search_book'),
    path('view_profile',views.view_profile,name='view_profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('profile_edit/<int:pk>',views.profile_edit,name='profile_edit'),
    path('suggestion_form',views.suggestion_form,name='suggestion_form'),
    path('suggestion_add',views.suggestion_add,name='suggestion_add'),
    path('show_suggestions',views.show_suggestions,name='show_suggestions'),









]