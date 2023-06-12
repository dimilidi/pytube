

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter
from pytube import YouTube
from pydub import AudioSegment
import urllib.request
from io import BytesIO
import os


def download_video():
    video_url = url_entry.get()

     # thumbnail_frame.configure(window, width=400)
   
    progressPercent.pack(side=tk.LEFT)
    progressPercent.configure(text="0%")
    finish_label.configure(text="") 
    progressBar.pack(side=tk.LEFT, padx=10)
    try:
        youtube = YouTube(video_url, on_progress_callback=on_progress)

        selected_format = format_var.get()
       
        if selected_format == "MP4":
            video = youtube.streams.get_highest_resolution()
            video.download()
            finish_label.configure(text="Video downloaded successfully!", text_color=("deeppink"))
           # messagebox.showinfo("Success", "Video downloaded successfully!")

        elif selected_format == "MP3":
            audio = youtube.streams.get_audio_only()
            if audio:
                audio_file = audio.download(filename_prefix='mp3_')
                # messagebox.showinfo("Success", "MP3 downloaded successfully!")
                mp3_file = convert_to_mp3(audio_file)
                os.remove(audio_file)  # Remove the temporary audio file
                finish_label.configure(text="MP3 downloaded successfully!", text_color=("deeppink"))
                # messagebox.showinfo("Success", "MP3 conversion completed!")
                # messagebox.showinfo("Success", f"MP3 saved at: {mp3_file}")
                return  # Return after converting to MP3
            else:
                finish_label.configure(text="The video does not have an audio-only option.",  text_color = "red")
                # messagebox.showerror("Error", "The video does not have an audio-only option.")
                return
        else:
            finish_label.configure(text="Please select a file format!", text_color = "red")
            # messagebox.showerror("Error", "Please select a file format!")
            return
        

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")




def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_percent = int(percentage_of_completion)

    # Update the progress bar
    progressBar.set(float(percentage_of_completion) / 100) # gives value between 0 and 1
    window.update_idletasks()

    # Update the progress label
    progressPercent.configure(text=f"{progress_percent}%")
    window.update_idletasks()




def convert_to_mp3(video_file):
    audio_file = video_file.split(".")[0] + ".mp3"
    audio = AudioSegment.from_file(video_file, format="mp4")
    audio.export(audio_file, format="mp3")
    return audio_file


def display_thumbnail():
    video_url = url_entry.get()
    finish_label.configure(text="")
    progressPercent.configure(text=f"")
    progressBar.set(0)
    progressBar.pack_forget()
    title_label.configure(text="")
    try:
        youtube = YouTube(video_url, on_progress_callback=on_progress)

        # display video title
        title = youtube.title
        if title:
            title_label.configure(text=title)  # Update the existing label's text
            title_label.pack(pady=10)
            
        else:
            url_label.configure(text="")

        thumbnail_url = youtube.thumbnail_url
        thumbnail_image = urllib.request.urlopen(thumbnail_url).read()
        thumbnail = ImageTk.PhotoImage(Image.open(BytesIO(thumbnail_image)).resize((250, 150)))
        thumbnail_label.configure(image=thumbnail)
        thumbnail_label.image = thumbnail
        thumbnail_label.pack()  # Show the label after configuring the image
        format_frame.pack(pady=10)
        download_button.pack()
        thumbnail_label.focus_set()  # Remove focus from the URL entry
    except Exception as e:
        thumbnail_label.pack_forget()  # Hide the label if an error occurs

# Create the main window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
window = customtkinter.CTk()
window.geometry("720x478")
window.title("YouTube Downloader")

# Create a frame to hold the URL entry and "Go" button
url_frame = customtkinter.CTkFrame(window, fg_color="transparent")
url_frame.pack(pady=0)

# Create a label and entry for the YouTube URL
url_label = customtkinter.CTkLabel(url_frame, text="YouTube URL:", font=("Helvetica", 16))
url_label.grid(row=0, column=0, columnspan=3, pady=10)

url_var = tk.StringVar()
url_entry = customtkinter.CTkEntry(url_frame, width=350, height=40, textvariable=url_var)
url_entry.grid(row=1, column=0, padx=10, pady=0)

# Create a "Go" button to fetch and display the thumbnail
go_button = customtkinter.CTkButton(url_frame, text="Go", command=display_thumbnail, width=40, height=40)
go_button.grid(row=1, column=1, padx=10, pady=0)


# Create a frame to hold the Thumbnail and the Video Title
thumbnail_frame = customtkinter.CTkFrame(window, fg_color="transparent")
thumbnail_frame.pack()

# Create a label to display the thumbnail image
thumbnail_label = customtkinter.CTkLabel(thumbnail_frame, text="")
thumbnail_label.pack_forget()

# Create a label to display the video title
title_label = customtkinter.CTkLabel(thumbnail_frame, text="")
title_label.pack(pady=0)

# Create a frame to hold the radio buttons
format_frame = customtkinter.CTkFrame(thumbnail_frame, height=40)
format_frame.pack_forget()

# Create radio buttons for format selection
format_var = tk.StringVar()
#format_var.set("MP4")

mp4_radio = customtkinter.CTkRadioButton(format_frame, text="MP4", variable=format_var, value="MP4", border_width_unchecked=2,  radiobutton_height=15, radiobutton_width=15)
mp4_radio.place(relx=0.44, rely=0.5, anchor=tk.CENTER)

mp3_radio = customtkinter.CTkRadioButton(format_frame, text="MP3", variable=format_var, value="MP3", border_width_unchecked=2, radiobutton_height=15, radiobutton_width=15)
mp3_radio.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

#format_frame.pack_propagate(0)


# Create a frame to hold the progress bar and percentage
progress_frame = customtkinter.CTkFrame(url_frame, height=27, width=0, fg_color="transparent")
progress_frame.grid(row=2, column=0, padx=0, pady=10)

# Create a progress bar
progressBar = customtkinter.CTkProgressBar(progress_frame, width=300)
progressBar.set(0)
progressBar.pack_forget()

# Create a label for progress bar and percentage
progressPercent = customtkinter.CTkLabel(progress_frame, text="")
progressPercent.pack_forget()

# Create a frame for button and finished downloading
download_frame = customtkinter.CTkFrame(window, height=50, fg_color="transparent")
download_frame.pack()

#Finished Downloading
finish_label = customtkinter.CTkLabel(download_frame, text="", text_color="blue")
finish_label.pack(padx=10, pady=10)

# Create a button to trigger the download
download_button = customtkinter.CTkButton(download_frame, text="Download", command=download_video, width=150, height=40)
download_button.pack_forget()

# Start the GUI main loop and update the progress periodically
window.mainloop()
