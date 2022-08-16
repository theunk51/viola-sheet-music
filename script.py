import os
from datetime import datetime



# filepath = /pdfs/

directory = "C:\\Users\\poptr\\Downloads\\Sheet\\website\\upload"
date = datetime.today()


with open("C:\\Users\\poptr\\Downloads\\Sheet\\website\\snippet.txt", "a") as f:
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            print('\n\n')
            print(filename)
            title = input("Title (Type NC if title = filename): ")
            if title.upper() == "NC":
                title = filename[:-4]

            subtitle = input("Subtitle (Type NA for None): ")
            if subtitle.upper() == "NA":
                subtitle = ''
            else:
                subtitle = f"\t\t<h2>{subtitle}</h2>"
            
            source = input("Source URL: ")


            code = f"""
            <div class="card">
                <div class="title">
                    <h1>{title}</h1>
            """ + subtitle + f"""
                </div>
                <div class="content">
                    <p>PDF: <a href="/pdfs/{filename}">{filename}</a></p>
                    <p>From: <a href="{source}">{source}</a></p>
                    <p>Date: {date.strftime("%m/%d/%y")}</p>
                </div>
            </div>
            """

            f.write(code)




# delete files after upload
print("done")






