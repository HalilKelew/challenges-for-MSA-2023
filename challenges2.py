#1.ask for file name
fileName = input("File Name: ")

#2.turn into all lowercase
fileName = fileName.lower()

#3.use an if statement to find the extention of it
if fileName.find(".gif") != -1:
    print("image/gif")
elif fileName.find(".jpg") != -1:
    print("image/jpg")
elif fileName.find(".jpeg") != -1:
    print("image/jpeg")
elif fileName.find(".png") != -1:
    print("image/png")
elif fileName.find(".pdf") != -1:
    print("document/pdf")
elif fileName.find(".txt") != -1:
    print("document/txt")
elif fileName.find(".zip") != -1:
    print("file/zip")
    #5. if the extension cannot be found, print an error.
else:
    print("application/octet-stream")

