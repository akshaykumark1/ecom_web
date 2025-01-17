# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')
    
    
    
    def login_user(req):
    if req.user.is_authenticated:
        return redirect(user_gallery)
    if req.method == 'POST':
         username = req.POST.get('username')
         password = req.POST.get('password')
         if not username or not password:
             messages.error(req, 'Please enter both username and password.')
             return redirect('login')
         user = authenticate(req, username=username, password=password)
         if user is not None:
             login(req, user)
             req.session['username']=user.username
             req.session['user_id']=user.id
             return redirect('user_gallery')
         else:
             messages.error(req, 'Invalid username or password.')
         
    

    return render (req,'login.html')
def signup(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirmpassword')

        if password == confirm_password:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    return render (req,'signup.html')
