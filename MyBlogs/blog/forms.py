from django import forms

from .models import Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {
            'id','title','content'
        }
        widgets = {
            'id': forms.TextInput(),
            'title': forms.TextInput(),
            'content': forms.Textarea()
        }
        labels = {
            'title':'Title',
            'content':'Content (Max: 5000 characters)'
        }


from .models import Author
class AuthorSignup(forms.ModelForm):
    class Meta:
        model = Author
        fields = {
            'author_name','avatar','description','password'
        }
        widgets = {
            'author_name':forms.TextInput(),
            'avatar': forms.TextInput(),
            'description': forms.Textarea(),
            'password':forms.PasswordInput()
        }
        label = {
            'author_name':'Author Name',
            'avatar':'Avatar',
            'description':'About Yourself',
            'password':'Enter Password'
        }



class AuthorSignIn(forms.ModelForm):
            class Meta:
                model = Author
                fields = {
                    'avatar',
                    'password'
                }
                widgets = {
                    'avatar': forms.TextInput(),
                    'password': forms.PasswordInput()
                }
                label = {
                    'avatar': 'Avatar',
                    'password': 'Enter Password'
                }


class Input(forms.Form):
    content = forms.TextInput()