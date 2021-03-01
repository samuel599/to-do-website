from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from posts.models import Post
from .forms import PostForm
from django.urls import reverse
import datetime
import pytz
# Create your views here.

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'users/home.html'
    context_object_name = 'posts'
    ordering = ['-datetime']

    def local_to_utc(self):
        time_zone = pytz.timezone('Asia/Kuala_Lumpur')



    def today_posts(self):
        start_time = date.time.combine(end_time,datetime.min.time())
        endtime = datetime.now()

    def get_queryset(self):
        #check post time is within today's times
        #today 00:00am datetime <= today 23:59pm
        #datetime.now()
        #

        my_date = datetime.datetime.now(pytz.timezone('US/Pacific'))
        today_min = datetime.datetime.combine(my_date, datetime.time.min)
        today_max = datetime.datetime.combine(my_date, datetime.time.max)
        print(today_min)
        print(today_max)

        local = pytz.timezone("America/Los_Angeles")
        local_min = local.localize(today_min, is_dst=None)
        local_max = local.localize(today_max, is_dst=None)

        utc_today_min = local_min.astimezone(pytz.utc)
        utc_today_max = local_max.astimezone(pytz.utc)
        print(utc_today_min)
        print(utc_today_max)


        #local = pytz.timezone("America/Los_Angeles")
        #naive = datetime.strptime("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
        #local_dt = local.localize(naive, is_dst=None)
        #utc_dt = local_dt.astimezone(pytz.utc)

        return Post.objects.filter(user=self.request.user, datetime__range=(utc_today_min, utc_today_max))



class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'




class PostCreateView(CreateView):
    model = Post
    fields = ['title','description','datetime']

'''
def create_post(request):
    user = request.user
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."

            user.user = request.user # Set the user object here
            user.save() # Now you can send it to DB

            return render_to_response("registration/complete.html", RequestContext(request))
    else:
        form = CreatePostForm()
    return render(request, 'registration/step3.html',)
'''

@login_required
def create(request):
    post = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #form.save()
            post = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."

            post.user = request.user # Set the user object here
            post.save() # Now you can send it to DB
            return redirect('/')
    else:
        form = PostForm()

    context = {'form':form}
    return render(request,'posts/post_form.html',context)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','description','datetime','complete']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False

    def get_success_url(self):
        return reverse('home')

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False

    def get_success_url(self):
        return reverse('home')
