from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView)
from django.conf import settings
from django.http import Http404

from apps.core.views import BaseView, LoginRequiredMixin
from apps.posts.models import Post
from apps.categories.models import Category

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests
import json
import re
import isodate

class PostListView(BaseView, ListView):
    template_name = 'posts/index.html'
    model = Post
    paginate_by = 15 

    def get_queryset(self):
        return Post.objects.order_by('-dateCreate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Bideox - Funny bideo'
            }
        }
        context.update(info)
        return context

class PostDetailView(BaseView, DetailView):
    template_name = 'posts/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name
            }
        }
        context.update(info)
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('id', 'name', 'description', 
                'videoDurationFe', 'category',)
    template_name = 'posts/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Submit video - Bideox'
            }
        }
        context['category'] = Category.objects.all()
        context.update(info)
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.profile = self.request.user.profile
        post.slug = self.get_slug(form.cleaned_data['name'])
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:index')

    def get_slug(self, str_input):
        str_input = str_input.lower().strip()

        str_input= re.sub(r'à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ',"a", str_input)
        str_input= re.sub(r'À|Á|Ạ|Ả|Ã|Â|Ầ|Ấ|Ậ|Ẩ|Ẫ|Ă|Ằ|Ắ|Ặ|Ẳ|Ẵ',"a", str_input)
        str_input= re.sub(r'è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ',"e", str_input)
        str_input= re.sub(r'È|É|Ẹ|Ẻ|Ẽ|Ê|Ề|Ế|Ệ|Ể|Ễ',"e", str_input)
        str_input= re.sub(r'ì|í|ị|ỉ|ĩ',"i", str_input)
        str_input= re.sub(r'Ì|Í|Ị|Ỉ|Ĩ',"i", str_input)
        str_input= re.sub(r'ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ',"o", str_input)
        str_input= re.sub(r'Ò|Ó|Ọ|Ỏ|Õ|Ô|Ồ|Ố|Ộ|Ổ|Ỗ|Ơ|Ờ|Ớ|Ợ|Ở|Ỡ',"o", str_input)
        str_input= re.sub(r'ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ',"u", str_input)
        str_input= re.sub(r'Ù|Ú|Ụ|Ủ|Ũ|Ư|Ừ|Ứ|Ự|Ử|Ữ',"u", str_input)
        str_input= re.sub(r'ỳ|ý|ỵ|ỷ|ỹ',"y", str_input)
        str_input= re.sub(r'Ỳ|Ý|Ỵ|Ỷ|Ỹ',"y", str_input)
        str_input= re.sub(r'đ|Đ',"d", str_input)
        str_input= re.sub(r'!|@|\$|%|\^|\*|\(|\)|\+|=|\&lt;|\&gt;|\?|\/|,|\.|\:|\'| |\"|\&amp;|\#|\[|\]|~',"-", str_input)
        str_input= re.sub(r'_',"-", str_input)
        str_input= re.sub(r' ',"-", str_input)
        str_input= re.sub(r'-+-',"-", str_input)
        str_input = str_input.strip('- ')
        return str_input
    
class CheckInfoYoutubeView(APIView):
    def get(self, request, format=None):
        url = request.GET.get('url', False)
        if url:
            data = self.get_info(url)
            return Response(data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_info(self, url):
        m = self.youtube_url_validation(url)
        if m:
            data = self.youtube_info_video(m)
            return data
        else:
            pass

    def youtube_url_validation(self, url):
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )

        youtube_regex_match = re.match(youtube_regex, url)
        if youtube_regex_match:
            return youtube_regex_match.group(6)

        return youtube_regex_match

    def youtube_info_video(self, youtube_id):
        url_request = "https://www.googleapis.com/youtube/v3/videos?part=snippet%2C+contentDetails&id="\
                                                         + youtube_id + "&key=" + settings.YOUTUBE_API_KEY
        response = requests.get(url_request)
        video_detail = json.loads(response.text)
        video_detail = video_detail['items'][0]
        data = {
            'id': youtube_id,
            'name': video_detail['snippet']['title'],
            'description': video_detail['snippet']['description'],
            'videoDurationFe': video_detail['contentDetails']['duration']            
        }
        dur = isodate.parse_duration(data['videoDurationFe'])
        data['videoDurationFe'] = str(dur)
        return data    
        

