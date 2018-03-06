import os,sys
import pdfkit

AHKin=sys.argv[1]
pythonIn=os.path.join(os.path.expanduser('~/Documents'),AHKin)
file_name=pythonIn+".pdf"
path_wkthmltopdf = r'C:\Python27\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
htmlist=[]
for i in range(6):
    htmlist.append(pythonIn+str(i)+".htm")

def save_pdf(htmls):
    options = {
    'encoding': 'UTF-8'
    }
    try:
        pdfkit.from_file(htmls, file_name,configuration=config, options=options)
    except:
        pass

save_pdf(htmlist)
for file in htmlist:
    os.remove(file)
    #shutil.move(file,os.path.join(srcpath,"_zrobione",AHKin))