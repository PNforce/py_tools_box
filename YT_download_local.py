from pytube import YouTube
#https://www.youtube.com/watch?v=1leXXHfaOFw

def YT_download(url, pixel="480p", type="mp4" ,path =""):
    #YouTube(url).streams.first().filter(subtype='mp4', pixel="720p").download()
    filename, msg = '', ''
    yt = YouTube(url)
    l_pixel = ['1080p', '720p', '480p', '360p', '240p', '144p']
    loc_pixel = l_pixel.index(pixel)

    filename = yt.title #find filename
    filename = remove_word_cant_be_file(filename)
    for loc in range(loc_pixel, len(l_pixel)):
        try:
            if type == "mp3":
                video = yt.streams.filter(file_extension=type).first()
            elif type == "mp4":
                video = yt.streams.filter(file_extension=type, res=l_pixel[loc], progressive=True).first()
            a = video.download(filename=filename)
            print('type a ', a)
            print('start dl ', filename)
            break
        except:
            if loc == 0:
                loc = 1
            msg = "only support {} resolution".format(l_pixel[loc-1])
        else:
            msg = "url error"

    r = {'msg': msg, 'filename': filename+'.'+type, 'path': path}
    print('')
    print('{}, {} download ok '.format(url, filename))
    return r

def remove_word_cant_be_file(str1):
    import re
    #a = re.findall(r'[^\*"/:?\\|<>]', str1, re.S)
    a = re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', str1, re.S)
    a = "".join(a)
    return a
if __name__ =="__main__":
    msg = ''
    type:str="mp4"
    solution='1080p'
    YTurl = "https://www.youtube.com/watch?v=5MAAVoOztF0"
    path = '/media/YTvideo/'  #localhost temp test, then rewrite to GCS route
    result = YT_download(YTurl, solution, type)
    
#b = remove_word_cant_be_file('John Dreamer - Brotherhood')
#print(b)

#YT_download('https://www.youtube.com/watch?v=1ieUf_sVPQQ','480p')
#https://github.com/nficano/pytube/issues/641
#YT_download('https://www.youtube.com/watch?v=B9vnv5cmn4M')
