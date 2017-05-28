# ページネーター
from django.core.paginator import (
    Paginator,  # ページネーター本体のクラス
    EmptyPage,  # ページ番号が範囲外だった場合に発生する例外クラス
    PageNotAnInteger  # ページ番号が数字でなかった場合に発生する例外クラス
)
from django.shortcuts import (
    render,
    redirect,
)
from .models import Posting
from .forms import PostingForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Posting.objects.all()
    return render(request, 'keijiban/post_list.html',{'posts': posts})

# スレッドを立てる(のちに削除予定)
def create_thread(request):
    # ModelFormもFormもインスタンスを作るタイミングでの使い方は同じ
    form = PostingForm(request.POST)
    """表示・投稿を処理する"""
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            # save()メソッドを呼ぶだけでModelを使ってDBに登録される。
            post.pk = 5
            post.save()
            # メッセージフレームワークを使い、処理が成功したことをユーザーに通知する
            messages.success(request, 'スレッドが作成されました。')
            return redirect('index',pk=post.pk)
        else:
            # メッセージフレームワークを使い、処理が失敗したことをユーザーに通知する
            messages.error(request, '入力内容に誤りがあります。')

    page = _get_page(
        Posting.objects.order_by('-id'),  # 投稿を新しい順に並び替えて取得する
        request.GET.get('page')  # GETクエリからページ番号を取得する
    )
    contexts = {
        'page': page,
        'form': form,
    }
    return render(request, 'keijiban/create_thread.html', contexts)

def _get_page(list_, page_no, count=100):
    """ページネーターを使い、表示するページ情報を取得する"""
    paginator = Paginator(list_, count)
    try:
        page = paginator.page(page_no)
    except (EmptyPage, PageNotAnInteger):
        # page_noが指定されていない場合、数値で無い場合、範囲外の場合は
        # 先頭のページを表示する
        page = paginator.page(1)
    return page

def index(request,pk):
    """表示・投稿を処理する"""
    post = get_object_or_404(Posting, pk=pk)
    # 教科名と投稿名者をフォームにあらかじめ登録しておく設定
    form = PostingForm(initial = {'subject':post.subject , 'name':post.name})
    if request.method == 'POST':
        # ModelFormもFormもインスタンスを作るタイミングでの使い方は同じ
        # form = PostingForm(request.POST, instance=post)
        form = PostingForm(request.POST or None)
        if form.is_valid():
            # save()メソッドを呼ぶだけでModelを使ってDBに登録される。
            form.save()
            post = form.save(commit=False)
            post.save()
            # メッセージフレームワークを使い、処理が成功したことをユーザーに通知する
            messages.success(request, '投稿を受付ました。')
            return redirect('index',pk=pk)
        else:
            # メッセージフレームワークを使い、処理が失敗したことをユーザーに通知する
            messages.error(request, '入力内容に誤りがあります。')

    page = _get_page(
        Posting.objects.order_by('-id'),  # 投稿を新しい順に並び替えて取得する
        request.GET.get('page')  # GETクエリからページ番号を取得する
    )
    contexts = {
        'page': page,
        # 'post': post,
        'form': form,
    }
    return render(request, 'keijiban/index.html', contexts)
