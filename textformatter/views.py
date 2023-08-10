from django.shortcuts import render, redirect
from .forms import blankForm, newAlbumForm, newSongForm
import json

def IndexView(request):
    result = ""
    data = dict()
    forms = {"New Album" : newAlbumForm(), "New Song" : newSongForm()}
    formShow = "New Album"

    print(result)


    if request.method == 'GET':
        try:
            if (request.GET.get("formShow")):
                formShow = request.GET.get("formShow")
            
            data['artist'] = request.GET.get("artist")
            data['twitterHandle'] = request.GET.get("twitterHandle")
            data['titleAlbum'] = request.GET.get("titleAlbum")
            data['titleTrack1'] = request.GET.get("titleTrack1")
            data['titleTrack2'] = request.GET.get("titleTrack2")
            data['trackNumber'] = request.GET.get("trackNumber")
            data['url'] = request.GET.get("url")

            result = (f"{data['artist']} @{data['twitterHandle']} ニューアルバムのすべての歌詞を読むことができます、「{data['titleAlbum']}」、@Genius で利用可能になりました。「{data['titleTrack1']}」、「{data['titleTrack2']}」含む全{data['trackNumber']}曲を収録💿\n\n🔗{data['url']}").strip()
        except(TypeError, IndexError):
            pass

    print(result)

    return render(request, "textformatter/index.html", {'result': result, 'forms':forms, 'formShow': formShow})

def NewSongView(request):
    result = ""
    form = newSongForm()
    data = dict()
    if request.method == 'GET':
        print(f"request is {request.GET}")
        try:
            data['artist'] = request.GET.get("artist")
            data['twitterHandle'] = request.GET.get("twitterHandle")
            data['titleTrack'] = request.GET.get("titleTrack")
            data['url'] = request.GET.get("url")

            result = (f"{data['artist']} @{data['twitterHandle']} 新曲「{data['titleTrack']}」 の歌詞情報が @Genius にて利用可能になりました。\n\n🔗{data['url']}").strip()
        except(TypeError, IndexError):
            pass

    print(result)

    # CARI INI RAK

    return render(request, "textformatter/index.html", {'result': result, 'form':form})