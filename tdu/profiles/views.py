from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import render, get_object_or_404
from .forms import UserProfileForm
from django.shortcuts import redirect

def profile_list(request):
    posts = UserProfile.objects.all()
    return render(request, 'profiles/profile_list.html', {'posts': posts})

def profile_detail(request, pk):
    post = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'profiles/profile_detail.html', {'post': post})

def profile_new(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid(): #誤った値が保存されていないかチェックする関数
            post = form.save(commit=False)
            post.save()
            return redirect('profile_detail', pk=post.pk)
            #URLじゃなくてname
    else:
        form = UserProfileForm()
    return render(request, 'profiles/profile_edit.html', {'form': form})

def profile_edit(request, pk):
    post = get_object_or_404(UserProfile, pk=pk)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('profile_detail', pk=post.pk)
    else:
        form = UserProfileForm(instance=post)
    return render(request, 'profiles/profile_edit.html', {'form': form})
