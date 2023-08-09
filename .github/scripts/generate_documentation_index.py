import os

directory = "path/to/your/directory"  # Update this with the actual path

with open("index.html", "w") as f:
    f.write("<html><body>\n")
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            f.write(f'<a href="{filename}">{filename}</a><br>\n')
    f.write("</body></html>\n")