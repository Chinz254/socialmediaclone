from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.models import User
from .models import Tweet

from .models import Tweet, Reply
from .forms import SignupForm, SigninForm, TweetForm


def tweet_lyk(request):
    twt = get_object_or_404(Tweet, id=request.POST.get('tweet_id'))
    twt.likes.add(request.user)
    return HttpResponseRedirect(reverse('account'))


def account(request):
    if request.user.is_authenticated:
        tweets = Tweet.objects.order_by('-created_on')
        user = User.username
        if request.method == 'POST':
            form = TweetForm(request.POST)
            if form.is_valid:
                new_post = Tweet(content=request.POST['content'])
                new_post.author = request.user
                new_post.save()
                return redirect('/')
        else:
            form = TweetForm()
        return render(request, 'twitter/index.html', {'tweets': tweets, 'form': form})
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = SignupForm(data=request.POST)
                signinform = SigninForm()

                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')
            else:
                signinform = SigninForm(data=request.POST)
                signupform = SignupForm()

                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')
        else:
            signupform = SignupForm()
            signinform = SigninForm()

        return render(request, 'twitter/signup.html', {'signupform': signupform, 'signinform': signinform})


def signout(request):
    logout(request)
    return redirect('/')
