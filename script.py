from pytube import YouTube
import tkinter as tk
import os
import time

def downloadFunction():


    name = entry_1.get() # Accept the link from the field of the input and record it into youtubeLink
    youtubeLink = YouTube(name) # Usage of YouTube package

    """Order by resolution, mp4 extension etc are some of the options for the downloaded song"""
    youtubeLink = youtubeLink.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if os.path.exists(" @@ Required path @@ ") == False: # Search if the directory exists
        os.makedirs(" @@ Required path @@ ")
    time1 = time.time()
    youtubeLink.download(" @@ Required path @@ ") # Download begins
    return(time.time()-time1) # Return the time that needed to be downloaded

def print_the_time():

        """ Here is a function which print the time that was needed to download his wishing song -- the time is counted in seconds"""
        print("You donwload it in ", str(downloadFunction())[:5], " seconds")



""" Here is the section which contains the creation of a window"""
main_window = tk.Tk()
main_window.title("Put whatever you want here...") # Title for the current window
main_window.geometry("400x150")

""" A label which welcome the user"""
label_1 = tk.Label(text="You can download any youtube video you want")
label_1.grid(column=0, row=0,)

""" A label which indicate where the user must paste the link of the song """
label_2 = tk.Label(text="Give me the link you want to download: ")
label_2.grid(column=0, row=1)

""" Input entry for the link of the preferred song """
entry_1 = tk.Entry()
entry_1.grid(column=1, row=1)

starting_time = time.time() # Counts the time that the script starts

""" After this button is clicked the download begins """
button_1 = tk.Button(text="Download it!", command=print_the_time)
button_1.grid(column=0, row=2)

.mainloop()
