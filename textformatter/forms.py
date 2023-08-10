from django import forms

class blankForm(forms.Form):
    adjective = forms.CharField(max_length=255, required=False)

class newAlbumForm(forms.Form):
    artist = forms.CharField(max_length=255, required=False, label='Artist Name')
    twitterHandle = forms.CharField(max_length=255, required=False, label='@Twitter')
    titleAlbum = forms.CharField(max_length=255, required=False, label='Album Title')
    titleTrack1 = forms.CharField(max_length=255, required=False, label='Track Title 1')
    titleTrack2 = forms.CharField(max_length=255, required=False, label='Track Title 2')
    trackNumber = forms.CharField(max_length=255, required=False, label='Number of Tracks')
    url = forms.CharField(max_length=255, required=False, label='Album URL')
    
class newSongForm(forms.Form):
    artist = forms.CharField(max_length=255, required=False, label='Artist Name')
    twitterHandle = forms.CharField(max_length=255, required=False, label='@Twitter')
    titleTrack = forms.CharField(max_length=255, required=False, label='Song Title')
    url = forms.CharField(max_length=255, required=False, label='Song URL')
