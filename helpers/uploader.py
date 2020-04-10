from youtube_upload.auth import GoogleAuth
from youtube_upload.youtube import Youtube

from config import Config

from translations import Messages as tr

import os
import time
import traceback

class Uploader:

    def __init__(self, file, title=None):
        
        self.file = file
        
        self.title = title


    async def start(self, progress=None, *args):
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message


    async def _upload(self):
        try:

            auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
            
            if not os.path.isfile(Config.CRED_FILE):
                self.status = False
                
                self.message = "Upload failed because you did not authenticate me."
                
                return

            auth.LoadCredentialsFile(Config.CRED_FILE)

            google = auth.authorize()

            properties = dict(
                title = self.title if self.title else os.path.basename(self.file),
                tags  =  'Entertainment,Kana TV,ያላለቀ ፍቅር፣,yalaleke fikir,amharic drama,kana drama,amharic movie,ferdegnochu,ethiopian movie,ende enat,yalaleke fikir recent,yalaleke fikir romantic,kana tv yalaleke fikir recent,yalaleke fikir saturday,yalaleke fikir season 2,kana tv yalaleke fikir saturday,kana tv yalaleke fikir full screen,yalaleke fikir today,yalaleke fikir today part,yalaleke fikir the last part,yalaleke fikir turkish,yalaleke fikir this week,yalaleke fikir tonight,yalaleke fikir turkey,yalaleke fikir today kana tv,kana tv yalaleke fikir this week,yalaleke fikir yesterday,yalaleke fikir yesterday part,yalaleke fikir youtube,yalaleke fikir kefel 1,yalaleke fikir part 1 fullscreen,yalaleke fikir part 1 kanal tv,' ,
                description = 'Kana-TV-|-Kana-drama-|-Kana-Abel-BirhanuTelevision-|-EBS-TV-WorldWide-|-JTV-Ethiopia-|-LTV-Ethiopia-|-ENN-Television|-New-Ethiopian-music-|-New-Ethiopian-Movie-|-Hope-Music-Ethiopia-|-GurshaTube-|-Entewawekalen-Wey-|-Zemen-Drama-|-Dana-drama-|-Welafen-drama-|Yesuf-App-Betoch-Comedy-|-Minew-Shewa-Tube-|-Sodere-TV-|-Arada-movies1|-EthioAddis-|-Official-Teddy-Afro-|-ESAT-TV-|-Ethiopia-|-Addis-Neger-|EthioTimes-|-AddisInfo-|-AddisOut-|-AddisTimes-|-CNN-|-BBC-|-Ethiopia-|Senselet-drama-|-Helen-bedilu-tube-|-New-Amharic-Drama-|-VOAAmharicDWAmharic|-Tenaadam-|-EthioTimes-|-EthioNow-|-Zehabesha-|-Hiber-Radio-|BBN-Radio-|-Admas-Radio-|-Yoni-Magna-|-Dire-Tube-|-Mogachoch,EthioTube-|-Dana-Drama-|-Derso-Mels-Drama-|-Ayer-Bayer-Drama-|-Amen-Drama-|-Meleket-Drama-|-Habesha-Movies-|-Habesha-Comedy-|-Arada-Cinema-|-Guragegna-Music-|-Oromigna-Music-|-Tigrigna-Music-|---AmharicMusic-|-Ethiopian-Music-|-DireTube|MinLitazez|Ethiopian-Comedy|Ethiopian-Drama|Ethiopian-Movies-|-Ethiopian-Music-Fana-Television-|-Nahoo-TV-|-Kana-TV-Kana-drama-|-EBS-TV-WorldWide-|JTV-Ethiopia-|-LTV-Ethiopia-|-ENN-Television-|New-Ethiopian-music-|-New-Ethiopian-Movie-|-Hope-Music-Ethiopia-|-Gursha-Tube-|-Entewawekalen-Wey-|-Zemen-Drama-|-Dana-drama-|-Welafen-drama-|-Betoch-Comedy-|-MinewShewa-Tube-|-Sodere-TV-|-Arada-movies1-|-EthioAddis-|-Official-Teddy-Afro-|ESAT-TV-|-Ethiopia-|-Addis-Neger-|-EthioTimes-|-JTV-Min-Addis-|-AddisOut-|AddisTimes-|-CNN-|-BBC-|-Ethiopia-|-Senselet-drama-|-Helen-bedilu-tube-|-NewAmharic-Drama-|-VOA-Amharic-|-DW-Amharic-|-Tenaadam-|-EthioTimes-EthioNow-|-Zehabesha-|-Hiber-Radio-|-BBN-Radio-|-Admas-Radio-|-YoniMagna,-Dire-Tube-|-Mogachoch,EthioTube-|-Dana-Drama-|-Derso-Mels-Drama|-Ayer-Bayer-Drama-|-Amen-Drama-|-Meleket-Drama-|-Habesha-Movies-|Habesha-Comedy-|-Arada-Cinema-|-Guragegna-Music-|-Oromigna-Music-|Tigrigna-Music-|-Amharic-Music-|-Ethiopian-Music|DireTube|MinLitazez|Ethiopian-Comedy|Jossy-In-The-House-Show-Yesuf-app-siraj-tech-yalaleke-fikr-ቃና-ቲቪ-Kana-|-Yegna-Sefer-የኛ-ሰፈር-|-yalaleke-fikir-ያላለቀ-ፍቅር-88-91-|-Tukir-Fikir-|-Ende-enat-እንደ-እናት-hd',
                category = 27,
                privacyStatus = 'public'
            )

            youtube = Youtube(google)

            self.start_time = time.time()
            self.last_time = self.start_time

            r = await youtube.upload_video(video = self.file, properties = properties)

            self.status = True
            self.message = f"https://youtu.be/{r['id']}"
        except Exception as e:
            traceback.print_exc()
            self.status = False
            self.message = f"Error occuered during upload.\nError details: {e}"
        return

