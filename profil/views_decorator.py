from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from common.views_main import home

def reqq_profil_login(request, mode):
    if (request.user.is_authenticated() == True) and (request.user.is_anonymous() == False) and (mode == True):
        if mode == True:
            return True
    elif mode == False:
        return True
    return False

def reqq_profil_in_group(request, group):
    if (request.user.is_authenticated() == True) and (request.user.is_anonymous() == False):
        if request.user.group.name == group:
            print("user is in group !")
            return True
    return False

def reqq_profil_confirmed(request, conf):
    if (request.user.is_authenticated() == True) and (request.user.is_anonymous() == False) and (request.user.is_confirmed == conf) :
        #print ("req = [" + conf + "] state = [" + request.user.is_confirmed + "]")
        return True
    return False

"""
check any user-related confiditions

login = True/False
check if the user must be logged in or out
if login == True the function will return user as second parameter between request and the other *args

group = "admin"
check if the user is in a group or not
require login = True !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

confirmed = True/False
check if the user is confirmed or not
require login = True !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""
def req_profil(var):

    def _method_wrapper(my_func):

        def _deco(request, *args, **kwargs):

            #login check
            return_profil = False
            if 'login' in var:
                print("login required with value [" + str(var['login']) + "]")
                if var['login'] == True:
                    check = reqq_profil_login(request, var['login'])
                    if check == False:
                        return redirect(home)
                    if var['login'] == True:
                        return_profil = True
            else:
                print("login not required")

            #group check
            if ('group' in var) and (return_profil == True):
                print("group required with value [" + var['group'] + "]")
                check = reqq_profil_in_group(request, var['group'])
                if check == False:
                    return redirect(home)
            else:
                print("group not required")

            #confirmed check
            if 'confirmed' in var and (return_profil == True):
                print("confirmed required with value [" + str(var['confirmed']))
                check = reqq_profil_confirmed(request, var['confirmed'])
                if check == False:
                    return redirect(home)
            else:
                print("confirmed not required")

            #return function
            if return_profil == True:
                return my_func(request, request.user, *args, **kwargs)
            else:
                return my_func(request, *args, **kwargs)
        return _deco
    return _method_wrapper
