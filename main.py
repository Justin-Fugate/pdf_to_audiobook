from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pyttsx3
import pdfplumber
import PyPDF2
from gtts import gTTS

Tk().withdraw()
filelocation = askopenfilename()

#Creating a PDF File Object
pdfFileObj = open(filelocation, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Get the number of pages
pages = pdfReader.numPages

string_of_text = ''

with pdfplumber.open(filelocation) as pdf:
 #Loop through the number of pages
    for i in range(0, pages):
      page = pdf.pages[i]
      text = page.extract_text()
      string_of_text += text
      #print(text)
      #speaker = pyttsx3.init()
      #speaker.say(text)
      #speaker.runAndWait()

final_file = gTTS(text=string_of_text, lang='en')  # store file in variable
final_file.save("loonshots.mp3")  # save file to computer