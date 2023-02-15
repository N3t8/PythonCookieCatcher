import http.cookies
import os
import sys

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
age = cookie.get("age")

sys.stdout.write("Content-Type: text/html\n\n")

if name is not None and age is not None:
    sys.stdout.write("<p>Name: %s</p>" % name.value)
    sys.stdout.write("<p>Age: %s</p>" % age.value)
else:
    sys.stdout.write("<p>No cookies</p>")
