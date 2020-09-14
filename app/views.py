from django.shortcuts import render
from django.core.paginator import InvalidPage, Paginator
from .forms import *
import smtplib
from django.core.mail import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders 
import requests
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.
def contact(request):
    contact_form = Contact(request.POST or None)
    response = requests.get('https://api.rootnet.in/covid19-in/contacts')
    data = response.json()
    context = {
        "title" : "contact",
        "contact_form": contact_form,
        "primary_number":data['data']['contacts']['primary']['number'],
        "primary_tollfree":data['data']['contacts']['primary']['number-tollfree'],
        "email":data['data']['contacts']['primary']['email'],
        "twitter":data['data']['contacts']['primary']['twitter'],
        "facebook":data['data']['contacts']['primary']['facebook'],
        "media":data['data']['contacts']['primary']['media'],
        "data":data['data']['contacts']['regional'],
    }
    mail=data['data']['contacts']['primary']['email']
    print(data['data']['contacts']['primary']['email'])
    if contact_form.is_valid():

        sender = contact_form.cleaned_data.get("sender")
        subject = contact_form.cleaned_data.get("subject")
        from_email = contact_form.cleaned_data.get("email")
        message = contact_form.cleaned_data.get("message")
        message = 'Sender:  ' + sender + '\nFrom:  ' + from_email + '\n\n' + message
        # send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=False)
        success_message = "We appreciate you contacting us, one of our Customer Service colleagues will get back" \
                          " to you within a 24 hours."
        messages.success(request, success_message)

        


        msg = MIMEText(message)
        
        msg['Subject'] = subject
        msg['From'] = 'contact.getskills@gmail.com'
        msg['To'] = mail

        # Create server object with SSL option  
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Perform operations via server
        server.login('piyushkumar0810@gmail.com', 'vikasgarg')
        server.sendmail('contact.getskills@gmail.com', [data['data']['contacts']['primary']['email']], msg.as_string())
        server.quit()

        return redirect(reverse('contact'))


    
    return render(request,'contact.html',context)

def notification(request):
    response=requests.get('https://api.rootnet.in/covid19-in/notifications')
    data=response.json()
    notifications=data['data']['notifications']
    page=[]
    for i in notifications:
        mydict={}
        if (i['title'][:2].isdigit and i['title'][2]=='.'):
            if (i['title'][3:5].isdigit() and i['title'][5]=='.'):
                if(i['title'][6:10].isdigit()):
                    mydict['date']=datetime.strptime(i['title'][:10], "%d.%m.%Y")
                    mydict['title']=i['title'][11:]
        else :
            mydict['title']=i['title']
            mydict['date']=""
        mydict['link']=i['link']
        page.append(mydict)
    paginator = Paginator(page, 10, orphans=2)
    is_paginated = True if paginator.num_pages > 1 else False
    page = request.GET.get('page') or 1
    try:
        current_page = paginator.page(page)
    except InvalidPage as e:
        raise Http404(str(e))
    context={
        'current_page':current_page,
        'is_paginated': is_paginated,
        # 'paginater':paginator
    }

    return render(request, 'notifications.html', context)


def hospital(request):
    response = requests.get('https://api.rootnet.in/covid19-in/hospitals/beds')
    data = response.json()
    # print(data)    
    context={
        'su':data['data']['summary'],
        'datas':data['data']['regional'],
    } 
    return render(request,'hospital.html',context)


def details(request):
    response = requests.get('https://api.rootnet.in/covid19-in/hospitals/medical-colleges')
    data = response.json()
    context={
        "datas":data["data"]["medicalColleges"],
    }
    return render(request,"medicalCollege.html",context)

def deaths(request):
    death_form=Death(request.POST or None)
    print('reached')
    # url='https://iitjodhpur.apps.dreamfactory.com/api/v2/cov19/_table/table%202'
    # response=requests.get(url,headers={'X-DreamFactory-API-Key':'ec81c498321f3023267bb60cb08d4de1c649638a6c5eb6c6e0f2c5e41ac3d6fa'})
    # data=response.json()
    if death_form.is_valid():
        state=death_form.cleaned_data.get("state")
        age_range=death_form.cleaned_data.get("age_range")
        gender=death_form.cleaned_data.get("gender")
        start_date=death_form.cleaned_data.get("start_date")
        end_date=death_form.cleaned_data.get("end_date")
        
        print(state)
        print(age_range)
        print(gender)
        print(start_date)
        print(end_date)
        # lst=[]
        # for i in data:
        #     p=True
        #     if(state!='India' and state!=i['state']):
        #         p=False
        #     if()
        # return redirect(reverse('deaths'))
    return render(request,'deaths.html',{'death_form':death_form})
    # print(data)