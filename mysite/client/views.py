from django.shortcuts import render, redirect
import requests

token = "38ac6c4728f9d801a075a16aff3f82d132a0e390"

# Create your views here.
def posts(request):
    r = requests.get('http://127.0.0.1:8000/posts')
    print(r.json())
    return render(request, 'posts.html', context={'posts': r.json()})


def post(request, post_id):
    r = requests.get(f'http://127.0.0.1:8000/posts/{post_id}')
    return render(request, 'post.html', context={'post': r.json()})


def new_post(request):
    if request.method == "POST":
        naujas_irasas = {
            'title': request.POST['title'],
            'body': request.POST['body'],
        }
        headers = {
            "Authorization" : f"Token {token}"
        }
        r = requests.post('http://127.0.0.1:8000/posts', data=naujas_irasas, headers=headers)
        return redirect("posts")
    else:
        return render(request, "new_post.html")
