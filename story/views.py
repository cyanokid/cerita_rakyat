from django.shortcuts import render, redirect, get_object_or_404
from .models import Story, Profile
from .forms import StoryForm, StoryFormUser, ProfileForm, UpdateUserForm
from members.forms import RegisterUserForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from datetime import datetime

#Import pagination stuff
from django.core.paginator import Paginator

# Create your views here.
# search bar
def search(request):
    if request.method == 'POST':

        searched = request.POST['searched']
        stories = Story.objects.filter(title__contains=searched)
        profiles = Profile.objects.filter(profile_bio__contains=searched)

        return render(request, 'story/search.html', {
            "searched" : searched,
            "stories" : stories,
            "profiles" : profiles,
            })
    else:
         return render(request, 'story/search.html', {
        
            })

#Admin Approval page
def admin_approval(request):
    #Get Story
    story_list = Story.objects.all()

    #Get counts
    num_story =  Story.objects.all().count()
    num_username =  Profile.objects.all().count()
    # user_count = User.objects.all().count()

    #get the current time
    now = datetime.now()
    time = now.strftime('%A, %d/%m/%Y, %I:%M %p')

    if request.user.is_superuser:
        if request.method == 'POST':

            #dapatkan id dari checkbox tadi, panggil guna nama dia 'boxes'
            id_list = request.POST.getlist('boxes')
            #Uncheck all events
            story_list.update(approved=False)
            #Update the database
            for x in id_list:
                Story.objects.filter(pk=int(x)).update(approved=True)

            messages.success(request, ("Kelulusan Admin Telah Dikemaskini."))   
            return redirect('home')

        else:   
            return render(request, 'story/admin_approval.html', {
            "story_list" : story_list,
            "time" : time,
            "num_story" : num_story,
            "num_username" : num_username,
        })
    else:
        messages.success(request, ("Anda tiada Kebenaran Untuk Melihat Paparan ini."))   
        return redirect('home')

    return render(request, 'story/admin_approval.html', {
        
    })

# Emoji for story
def story_shock(request, pk):
    if request.user.is_authenticated:
        story = get_object_or_404(Story, id=pk)

        # logic for like and unlike
        #if people that click already associated/already likes
        if story.shocks.filter(id=request.user.id):
            story.shocks.remove(request.user)
        #if people that click not associated/ likes yet. then it will likes if click
        else:
            story.shocks.add(request.user)

        # redirect to the previous page using HTTP_REFERER
        return redirect(request.META.get("HTTP_REFERER"))
        
    else:
        return redirect('home')
        messages.success(request, ("Anda perlu log Akaun Untuk Menyukai Paparan Ini."))

def story_angry(request, pk):
    if request.user.is_authenticated:
        story = get_object_or_404(Story, id=pk)

        # logic for like and unlike
        #if people that click already associated/already likes
        if story.angrys.filter(id=request.user.id):
            story.angrys.remove(request.user)
        #if people that click not associated/ likes yet. then it will likes if click
        else:
            story.angrys.add(request.user)

        # redirect to the previous page using HTTP_REFERER
        return redirect(request.META.get("HTTP_REFERER"))
        
    else:
        return redirect('home')
        messages.success(request, ("Anda perlu log Akaun Untuk Menyukai Paparan Ini."))

def story_laugh(request, pk):
    if request.user.is_authenticated:
        story = get_object_or_404(Story, id=pk)

        # logic for like and unlike
        #if people that click already associated/already likes
        if story.laughs.filter(id=request.user.id):
            story.laughs.remove(request.user)
        #if people that click not associated/ likes yet. then it will likes if click
        else:
            story.laughs.add(request.user)

        # redirect to the previous page using HTTP_REFERER
        return redirect(request.META.get("HTTP_REFERER"))
        
    else:
        return redirect('home')
        messages.success(request, ("Anda perlu log Akaun Untuk Menyukai Paparan Ini."))


def story_sad(request, pk):
    if request.user.is_authenticated:
        story = get_object_or_404(Story, id=pk)

        # logic for like and unlike
        #if people that click already associated/already likes
        if story.sads.filter(id=request.user.id):
            story.sads.remove(request.user)
        #if people that click not associated/ likes yet. then it will likes if click
        else:
            story.sads.add(request.user)

        # redirect to the previous page using HTTP_REFERER
        return redirect(request.META.get("HTTP_REFERER"))
        
    else:
        return redirect('home')
        messages.success(request, ("Anda perlu log Akaun Untuk Menyukai Paparan Ini."))


def story_like(request, pk):
    if request.user.is_authenticated:
        story = get_object_or_404(Story, id=pk)

        # logic for like and unlike
        #if people that click already associated/already likes
        if story.likes.filter(id=request.user.id):
            story.likes.remove(request.user)
        #if people that click not associated/ likes yet. then it will likes if click
        else:
            story.likes.add(request.user)

        # redirect to the previous page using HTTP_REFERER
        return redirect(request.META.get("HTTP_REFERER"))
        
    else:
        return redirect('home')
        messages.success(request, ("Anda perlu log Akaun Untuk Menyukai Paparan Ini."))

def profile_list(request):
    if request.user.is_authenticated:

        #Set up pagination
        p = Paginator(Profile.objects.exclude(user=request.user), 10)
        page = request.GET.get('page')
        profiles_list = p.get_page(page)
        #for pagination hack to show all pages
        nums = "a" * profiles_list.paginator.num_pages

        profiles = Profile.objects.exclude(user=request.user)   # To exclude my profile
        return render(request, 'story/profile_list.html', {
            "profiles" : profiles,
            "profiles_list" : profiles_list,
            "nums" : nums,
        })
    else:
        messages.success(request, ("Anda perlu log Akaun Untuk Melihat Paparan Ini."))
        return redirect('home')


        
def update_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        #take the info from user in that form
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile_user)
        if request.method == "POST":
            if user_form.is_valid and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                
                login(request, current_user)
                messages.success(request, ("Profil Anda Telah Dikemaskini."))
                return redirect('home')
        else:
            return render(request, 'story/update_profile.html', {
                "user_form" : user_form,  
                "profile_form" : profile_form,   
            })
    else:
        return redirect('home')
        messages.success(request, ("Anda perlu log Akaun Untuk Melihat Paparan Ini."))


def show_profile(request, pk):
    if request.user.is_authenticated:
        me = request.user.id
        profile = Profile.objects.get(user_id=pk)
        stories =  Story.objects.filter(creator=me).order_by("-created_at")
        return render(request, 'story/show_profile.html', {
            "profile" : profile,
            "stories" : stories,
        }) 

    else:
        messages.success(request, ("Anda perlu log Akaun Untuk Melihat Paparan Ini."))
        return redirect('home')

def delete_story(request, story_id):
    story = Story.objects.get(pk=story_id)
    if request.user == story.creator:
        story.delete()
        messages.success(request, ("Perkongsian Anda telah Dihapuskan."))
        return redirect('my_story')
    else:
        messages.success(request, ("Anda tiada Kebenaran Untuk Menghapus Perkongsian Ini."))
        return redirect('my_story')

def my_story(request):
    if request.user.is_authenticated:
        me = request.user.id
        stories =  Story.objects.filter(creator=me) 

        #Set up pagination
        p = Paginator(Story.objects.filter(creator=me), 5)
        page = request.GET.get('page')
        storys = p.get_page(page)
        #for pagination hack to show all pages
        nums = "a" * storys.paginator.num_pages

        return render(request, 'story/my_story.html',{
            "stories" : stories, 
            "storys": storys,
            "nums" : nums,
        })
    else:
        messages.success(request, ("Anda tiada Kebenaran Untuk Melihat Paparan ini."))   
        return redirect('home')

def add_story(request):
    submitted = False
    if request.method == "POST":

        if request.user.is_authenticated:

            form = StoryFormUser(request.POST)    
            if form.is_valid():
                form = form.save(commit=False)
                #auto fill creator with user
                form.creator = request.user
                #auto fill username with user
                form.username = request.user
                #auto fill email with user email
                form.email = request.user.email
                form.save()
                return HttpResponseRedirect('/add_story?submitted=True')

        else:

            form = StoryForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                #auto fill creator with user
                form.save()
            
                # form.save()
                return HttpResponseRedirect('/add_story?submitted=True')

        # form = StoryForm(request.POST)

        # if form.is_valid():
        #     form = form.save(commit=False)
        #     #auto fill creator with user
        #     if request.user.is_authenticated:
        #         form.creator = request.user
        #     form.save()
            
        #     # form.save()
        #     return HttpResponseRedirect('/add_story?submitted=True')

    else:
        if request.user.is_authenticated:
            form = StoryFormUser

        else:
            form = StoryForm

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'story/add_story.html', {
        "form" : form,
        "submitted" : submitted,
    })

def show_story(request, story_id):
    #pass specific object from venue model
    story = Story.objects.get(pk=story_id)
    
    return render(request, 'story/show_story.html',{
        "story" : story,
    })

def home(request):
    #get all story model
    stories = Story.objects.all()

    #Set up pagination
    p = Paginator(Story.objects.all(), 10)
    page = request.GET.get('page')
    storys = p.get_page(page)
    #for pagination hack to show all pages
    nums = "a" * storys.paginator.num_pages

    return render(request, 'story/home.html', {
        "stories" : stories,
        "storys" : storys,
        "nums" : nums,
    })


