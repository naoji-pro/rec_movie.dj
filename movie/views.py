from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm


def frontpage(request):
    return render(request, "frontpage.html")


def view1(request):
    post = Post.objects.get(title="大学生3人の友情に心を打たれ、感動すること間違いなし！")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view1')
    else:
        form = CommentForm()
    context = {
        'message1': 'きっとうまくいくのレビューページ',
        'post': post,
        'form': form
    }
    return render(request, 'pages.html', context)


def view2(request):
    post = Post.objects.get(title="ラストにまさかの展開で鳥肌が立った。")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view2')
    else:
        form = CommentForm()
    context = {
        'message1': '女神の見えざる手のレビューページ',
        'post': post,
        'form': form
    }
    return render(request, 'pages.html', context)


def view3(request):
    post = Post.objects.get(title="SFドラマではあるが実はそれだけじゃない！")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view3')
    else:
        form = CommentForm()
    context = {
        'message1': 'インターステラーのレビューページ',
        'post': post,
        'form': form
    }
    return render(request, 'pages.html', context)

def view4(request):
    post = Post.objects.get(title="まさに狂気！だが、それが見どころ！")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view1')
    else:
        form = CommentForm()
    context = {
        'message1': 'セッションのレビューページ',
        'post': post,
        'form': form
    }
    return render(request, 'pages.html', context)


def view5(request):
    post = Post.objects.get(title="人種は違えど、友情は素晴らしい！")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view2')
    else:
        form = CommentForm()
    context = {
        'message1': 'グリーンブックのレビューページ',
        'post': post,
        'form': form
    }
    return render(request, 'pages.html', context)


def view6(request):
    post = Post.objects.get(title="本物の天才が国家を救う！")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view3')
    else:
        form = CommentForm()
    context = {
        'message1': 'イミテーション・ゲームのレビューページ',
        'post': post,
        'form': form
    }
    return render(request, 'pages.html', context)