from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


Folder_name = ''
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text = Folder_Name, fg = 'green')

    else:
        locationError.config(text = 'please choose folder!!', fg = 'red')

#download video
def downloadvideo():
    choice= ytchoices.get()
    url = ytEntry.get()

    if(len(url)>1):
        yterror.config(text ='')
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive = True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            yterror.config(text = 'paste link again!!', fg = 'red')

#download function
    select.download(Folder_name)
    yterror.config(text = 'download complete!!')
root = Tk()
root.title('yt downloader')
root.geometry('350x400')
root.columnconfigure(0,weight=1)#set all content in center.
#youtube_logo=PhotoImage(file='yt icon.png'),
#root.iconphoto(False,youtube_logo)

#yt link label
ytLabel = Label(root,text = 'enter the url of the video baka',font = ('ariel',15))
ytLabel.grid()

#entry box
ytEntryVar = StringVar()
ytEntry = Entry(root, width = 50, textvariable=ytEntryVar)
ytEntry.grid()

#error message
yterror = Label(root, text = 'Error msg', fg = 'red', font = ('ariel', 15))
ytEntry.grid()

#asking save file label
saveLabel = Label(root, text = 'save the video file', font = ('ariel', 15, 'bold'))
saveLabel.grid()

#btn of save file
saveEntry = Button(root, width = 10, bg = 'blue', fg = 'red', text = 'choose path', command = openLocation)
saveEntry.grid()

#error msg location
locationError = Label(root, text = 'Error msg of path', fg = 'blue', font = ('ariel', 10))
locationError.grid()

#download quality
ytQuality = Label(root, text = 'select Quality', font = ('ariel', 15))
ytQuality.grid()

#combobox
choices = ('1080p', '720p', '144p', 'only audio')
ytchoices = ttk.Combobox(root, values = choices)
ytchoices.grid()

#download btn
downloadbtn = Button(root, text = 'download', width = 10, bg = 'red', fg = 'white', command = downloadvideo)
downloadbtn.grid()

#group name label
groupnamelabel = Label(root, text = 'yoruba demons', font = ('ariel', 10))
groupnamelabel.grid()


def print_progressbar(total, current, barsize = 60):
    progress = int(current*barsize/total)
    completed = str(int(current*100/total)) + '%'
    print('[', chr(9608)*progress, '', completed, '.'*(barsize-progress), ']', str(i)+'/'+str(total), sep='', end='\r', flush=True)
root.mainloop()
