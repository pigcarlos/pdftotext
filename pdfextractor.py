from tkinter import*
from PIL import Image, ImageTk 
import PyPDF2 
from PyPDF2 import *
from PyPDF2.pdf import PageObject
from tkinter.filedialog import askopenfile

window = Tk()
window.title("PDF extract application")

canvas = Canvas(window, width=650, height=250)
canvas.grid(columnspan=3,rowspan=3)

#logo
logo = Image.open("turn (5).png")
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image= logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = Label(window, text="Select a PDF file on your computer to extract all text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

#function
def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=window,mode="rb", title="Choose file", filetypes=[("Pdf file", "*.pdf")])

    if file :
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = PageObject.extractText(page)
        
        #Text Box
        text_box = Text(window, height=10, width=50, padx=10, pady=15)
        text_box.insert(1.0, page_content)
        text_box.grid(column=1, row=3)

        browse_text.set("Browse") 
       
#Buttons
browse_text = StringVar()
browse_button = Button(window, textvariable= browse_text,command=lambda:open_file(),font="Raleway", bg="#38B6FF", fg="white")
browse_text.set("Browse")
browse_button.grid(column=1, row=2) 

canvas = Canvas(window, width=650, height=300)
canvas.grid(columnspan=3,)

window.mainloop()