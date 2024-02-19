from django.shortcuts import render
from . import forms


def feedbackview(request):
    form=forms.Feedback()
    if request.method=='POST':
        form=forms.Feedback(request.POST)
    
        if form.is_valid():
            print(form.cleaned_data)
            # print('form validation succes and printing feedback information')
            # print('Student name      :-',form.cleaned_data['name'])
            # print('Student Rollno    :-',form.cleaned_data['rollno'])
            # print('Student mail id   :-',form.cleaned_data['email'])
            # print('Student Feedback  :-',form.cleaned_data['feedback'])
            my_dict={'name':form.cleaned_data[0]}
            return render(request,'fdtemplates/thanks.html',context=my_dict)
    return render(request,'fdtemplates/home.html',{'form':form})
