import requests
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from urllib.request import urlopen



base_url_starter = "https://api.mangadex.org"
ret_item = requests.get(base_url_starter + "/at-home/server/463e9ee0-b75b-4c74-a764-74382f4db183")
ret_item2 = ret_item.json()
#print(ret_item2)


main_window = tk.Tk()
main_window.title("Karakai Jouzu no (Moto) Takagi-San")


main_frame = ttk.Frame(main_window, padding = 10)
main_frame.grid()


pg1 = ret_item2['baseUrl'] + '/data-saver/' + ret_item2['chapter']['hash'] + '/' + ret_item2['chapter']['dataSaver'][1]
img = Image.open(requests.get(pg1, stream=True).raw)

# img = img.resize((1920,1080), Image.ANTIALIAS)


photo = ImageTk.PhotoImage(img)



ttk.Label(main_frame, image = photo).grid(column=0, row=0)
ttk.Button(main_frame, text="Quit", command=main_window.destroy).grid(column=0, row=1)

main_window.mainloop()
