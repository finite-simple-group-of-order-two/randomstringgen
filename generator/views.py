from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    dict_to_page = {"range" : list(range(10,21))}
    return render(request, 'generator/home.html', dict_to_page)

def password(request):
    # Getting the length of password entered by user
    l = int(request.GET['length'])

    # If someone decides to do a sneaky this will change length to the max allowed upper bound
    if (l>20):
        l=20

    # Getting all the boolean flags that are stored as strings cuz django; they're either "on" or None
    upc = request.GET.get('uppercase')  # gets the uppercase checkbox status
    num = request.GET.get('numbers')    # gets the numbers checkbox status
    spl = request.GET.get('special')    # gets the special checkbox status

    # Django communicates with webpages in json format, we just pass in a dict, here initialising it
    dict_to_page = {'generated_password' : '',
                    'upc_checkbox' : '',
                    'num_checkbox' : '',
                    'spl_checkbox' : '',
                    'range' : list(range(10,21)),
                    'prev' : l
                    }
    
    # The default list containing characters that the random string will be generated out of
    chars = list('abcdefghijklmnopqrstuvwxyz')

    # Adding the list of other characters to the default one as per the checkboxes
    if upc == 'on':
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        dict_to_page['upc_checkbox'] = 'checked'
    if num == 'on':
        chars.extend(list('0123456789'))
        dict_to_page['num_checkbox'] = 'checked'
    if spl == 'on':
        chars.extend(list('!@#$%^&*()_+|}{:"?><'))
        dict_to_page['spl_checkbox'] = 'checked'
    
    # Setting default blank password
    passw=''

    # Looping for as many times as the length, adding a randomly picked character from the list to the final string
    for _ in range (l):
        passw+=random.choice(chars)

    # Setting the generated password key in the dict we'll send to page
    dict_to_page['generated_password'] = passw

    #finally rendering the webpage
    return render(request, 'generator/password.html', dict_to_page)
    
def license(request):
    return render(request, 'generator/license.html')
