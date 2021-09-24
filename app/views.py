from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def not_string(request, str):
  if len(str) >= 3 and str[:3] == "not":
    return HttpResponse(str)
  return HttpResponse("not " + str)

def make_abba(request, a, b):
  return HttpResponse(a + b + b + a)

def close_far(request, a, b, c):
  cond1 = abs(a-b) <= 1 and abs(b-c) >=2 and abs(a-c) >= 2
  cond2 = abs(a-c) <= 1 and abs(a-b) >=2 and abs(c-b) >= 2
  return HttpResponse(cond1 or cond2)
