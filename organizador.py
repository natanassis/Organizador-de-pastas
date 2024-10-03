import os 
import shutil
from pathlib import Path
from tkinter import messagebox, Tk, Label, Entry, Button





def organizador_pastas():
    path = website_entry.get()
    downloads_folders_path =Path(fr"{path}")


    print(downloads_folders_path)

    for file in os.listdir(downloads_folders_path):
        filename, file_extension = os.path.splitext(file)#
        file_extension = file_extension[1:]
        #print(filename,file_extension)

        folder_to_organize_file = f"{downloads_folders_path}/{file_extension}"

        if not os.path.isdir(folder_to_organize_file):
            os.mkdir(folder_to_organize_file)

        shutil.move(f"{downloads_folders_path}/{file}", f"{folder_to_organize_file}/{file}")
        

if __name__ == '__main__':
    window = Tk()
    window.title("Organizador de Pastas")
    window.config(padx=10, pady=100)

    # Labels
    website_label = Label(text="Endereço:")
    website_label.grid(row=2, column=0)

    # Entries
    website_entry = Entry(width=35)
    website_entry.grid(row=2, column=1, columnspan=2)
    website_entry.focus()
    add_button = Button(text="Caminho da Pasta", width=36, command=organizador_pastas)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()