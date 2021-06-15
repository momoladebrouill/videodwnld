import youtube_dl,time
from urllib.request import urlopen
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os

L=""
"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
"id	uploader	uploader_id	uploader_url	channel_id	channel_url	upload_date	license	creator	title	alt_title	thumbnails	description	categories	tags	subtitles	automatic_captions	duration	age_limit	annotations	chapters	webpage_url	view_count	like_count	dislike_count	average_rating	formats	is_live	start_time	end_time	series	season_number	episode_number	track	artist	album	release_date	release_year	extractor	webpage_url_basename	extractor_key	playlist	playlist_index	thumbnail	display_id	requested_subtitles	requested_formats	format	format_id	width	height	resolution	fps	vcodec	vbr	stretched_ratio	acodec	abr	ext"
def ytb_dwl(lien,telch=False,audio=False):

        ydl_opts={'outtmpl': '%(title)s.%(ext)s'}
        if audio:
            ydl_opts['format']='bestaudio/best'
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        with ydl:
            result = ydl.extract_info(lien,download=telch)
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result

        return video


def image_png(video):
    b=urlopen(video["thumbnail"]).read()
    f=open('webm.png','wb')
    f.write(b)
    f.close()
    time.sleep(0.5)


def init():
    global L
    L=e.get()
    f.destroy()
    v=ytb_dwl(L)
    imag=image_png(v)
    print(imag)
    touka(v,imag)


def touka(video,img):
    global f
    f = Tk()
    f.title("Yay télécharger !!!")
    img=Image.open("webm.png")
    img=img.resize((int(img.width//4),int(img.height//4)))
    img = ImageTk.PhotoImage(img)
    c = Canvas(f, width = img.width(), height = img.height())
    c.create_rectangle(0,0,img.width(),img.height(),fill="black")
    c.create_image(0, 0, anchor=NW, image=img)
    info=Frame(f)
    l=Label(info,
            text=video["title"]+
            "\nVidéo offerte par "+video["uploader"]+"\n"+
            "{:,}".format(video["view_count"])+" vues"+"\n"+
            "{:,}".format(video["like_count"])+" likes")
    b=Button(info,text="Télécharger video",command=action_vid)



    l.pack()
    b.pack()
    c.grid(row=0,column=0)
    info.grid(row=0,column=1)
    f.mainloop()


def action_vid():
    global L
    ytb_dwl(L,True)
    f.destroy()
    defi()
def action_aud():
    global L
    ytb_dwl(L,True,True)
e,f=None,None
def defi():
    global e,f
    f=Tk()
    l=Label(f,text='Bienvenue sur mon installeur youtbue tabernak !\n Et du coup il faut coller le lien de la video ici :')
    e=Entry(f,text="le lien ici")
    b=Button(f,text="Valider",command=init)
    l.pack(padx=34)
    e.pack()
    b.pack(pady=5)
    f.mainloop()
if __name__=="__main__":
    defi()
