from django import forms 
from django.core import validators
from . import models

# def checker(value):
#     if value[0]=='D':
#         return value
#     else:
#         raise forms.ValidationError('Dont do that')

class Feedback(forms.ModelForm):
    class Meta:
        model=models.Employee
        # fields=('field1','field2','field3','field4')
        # exclude=('field1','field2','field3','field4')
        fields='__all__'
    name=forms.CharField()
    email=forms.EmailField()
    rollno=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    password1=forms.CharField(label='password(again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print('total Form validation')
        cleaned_data=super().clean()
       
        inputpass=cleaned_data['password']
        inputpass1=cleaned_data['password1']
        bot_hanndler_val=cleaned_data['bot_handler']
        if inputpass==inputpass1:
            if len(inputpass)<4:
                raise forms.ValidationError("please enter large size password")
            else :
                return inputpass
        else:
            raise forms.ValidationError("password should be matched")

        if (bot_hanndler_val)!=0:
            raise forms.ValidationError('thanks bot you are nothing infront of me')


    # def clean_name(self):
    #     inputname=self.cleaned_data['name']
    #     if len(inputname)<4:
    #         raise forms.ValidationError('The length of name should be greater than equal to 4')
    #     else :return inputname

    # def clean_email(self):
    #     emaill=self.cleaned_data('email')
    #     if len(emaill)<=4:
    #         raise forms.ValidationError("INVAlID EMAil")


