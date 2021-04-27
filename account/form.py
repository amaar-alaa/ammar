from django import forms  




class Subscribe(forms.Form):
    name=forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={
        "placeholder":"Name",
        "class":"contact__input"}))


    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder":"Email",
             "class":"contact__input",
             "type":"mail"}))
  
    message=forms.CharField(max_length=500,
        widget=forms.Textarea(attrs={
            "placeholder":"Message",
            "class":"contact__input",
            "cols":"0", 
            "rows":"10"}))