from django import forms
from datetime import date

AGE_Range=[
    ('00-09','0-9'),
    ('10-19','10-19'),
    ('20-29','20-29'),
    ('30-39','30-39'),
    ('40-49','40-49'),
    ('50-59','50-59'),
    ('60-69','60-69'),
    ('70-1000','70+')
]

States=[
    ('India','India'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Chandigarh','Chandigarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman & Diu','Daman & Diu'),
    ('Delhi','Delhi'),
    ('Lakshadweep','Lakshadweep'),
    ('Puducherry','Puducherry'),
]

Gender=[
    ('male','Male'),
    ('female','Female'),
    ('na','NA'),
]

class Contact(forms.Form):
    sender = forms.CharField(label='Name', max_length=30)
    subject = forms.CharField(label='Subject', max_length=30)
    email = forms.EmailField(label='Email', max_length=30)
    message = forms.CharField(widget=forms.Textarea)

  
class Death(forms.Form):
    state=forms.CharField(widget=forms.Select(choices=States))
    age_range= forms.CharField(initial='0',widget=forms.Select(choices=AGE_Range))
    gender=forms.CharField(initial = 'NA',widget=forms.Select(choices=Gender))
    start_date= forms.DateField(label='Start Date', initial="2020-01-01", widget=forms.SelectDateWidget(years=[2020]))
    end_date= forms.DateField(label='End Date', initial=date.today(), widget=forms.SelectDateWidget(years=[2020]))


