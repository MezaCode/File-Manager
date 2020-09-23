#     File Manager (updated version) created by Mazen Shaban.
#         this program is meant for me to continue to work on it as the need arises and new conditions enter my life.

import os
import shutil
import ntpath

Desktop = r'C:\Users\Mazen\Desktop' #Location that I want to manage
Downloads = r'C:\Users\Mazen\Downloads'#second location that i want to manage

rootDomain = r'I:\Current' #root of where to start moving files to

category = "empty"  # used to keep track of which category we are entering

moveToDir = r'I:\Current' # used for knowing where to move each file to.




# over here create lists for each of the inner most folders
#     example I:\Current\MyLife\Finances contains \bills  \receipts  \ taxes
#    you'll create a list of key words for bills, one for receipts and one for taxes
#finances category
Bills = ["bill", "Bill", "BILL"]
Tax = ["tax", "Tax", "TAX"]
Receipts = ["receipt", "Receipt", "RECEIPT", "invoice", "Invoice", "INVOICE", "order", "Order", "ORDER"]
#college category
HW = ["HW", "Homework", "HOMEWORK"]
Quiz = ["quiz", "Quiz", "QUIZ"]
Project = ["Project", "project", "proj", "Proj", "PROJECT", "PROJ"]
Labs = ["lab", "Lab", "LAB", "assign", "Assign", "ASSIGN"]
#Media category
Photo = [".jpg", ".jpeg", ".JPEG", ".JPG", ".png", ".PNG", ".gif", ".GIF", ".nef", ".NEF"]
Video = [".webm", ".WEBM", ".mpg", ".MPG", ".mkv", ".MKV", ".mp4", ".MP4", ".avi", ".AVI", ".mov", ".MOV"]
docs = [".pdf", ".PDF", ".doc", ".DOC"]
Audio = [ ".mp3", ".MP3"]
#Health category
Health = ["dental", "medical", "Dental", "DENTAL", "Dentist", "dentist", "DENTIST", "Medical", "MEDICAL"]
Home = ["lease", "rent", "Lease", "LEASE", "Rent", "RENT"]
Travel = ["travel", "Travel", "TRAVEL", "ticket", "Ticket", "TICKET", "itinerary", "Itinerary", "ITINERARY", "flight", "Flight", "FLIGHT"]
# over here combine the inner most into the next layer
#     example create a list for finances and add together the arrays for bills, receipts and taxes
#     into that array
CS3343 = ["CS3343", "CS 3343", "cs 3343", "cs3343"]
CS3733 = ["CS3733", "CS 3733", "cs 3733", "cs3733"]
CS3773 = ["CS3773", "CS 3773", "cs 3773", "cs3773"]
CS3853 = ["CS3853", "CS 3853", "cs 3853", "cs3853"]
Finances = Bills + Tax + Receipts
# over here do the next layer
#  example I:\Current\MyLife contains Finances, Health, Home, Personal & travel
#  add all those into a list called MyLife
MyLife = Finances + Health + Home + Travel
College = CS3343 + CS3733 + CS3773 + CS3853 + HW + Quiz + Project + Labs + ["gwi764", "GWI764", "Gwi764"]
Career = ["cv", "CV", "resume", "Resume", "RESUME"]
Media = Photo + Video + docs + Audio



file = [] # list to hold file names

for root, subdirs, files in os.walk(Desktop):# for each loop to grab files from downloads dir and its subdirs
    for f in files:
        file.append(os.path.join(root,f))# grab file name, join it with it's directory location then append it to a list for files



for root, subdirs, files in os.walk(Downloads): # for each loop to grab files from downloads dir and its subdirs
    for f in files:
        file.append(os.path.join(root,f)) # grab file name, join it with it's directory location then append it to a list for files


# begin sorting
for f in file:

    if category == "empty":
        for key in MyLife:
            if key in f:
                category = "MyLife"
                moveToDir = r'I:\Current\MyLife'
    if category == "empty":
        for key in Career:
            if key in f:
                category = "Career"
                moveToDir = r'I:\Current\Career'
    if category == "empty":
        for key in College:
            if key in f:
                category = "College"
                moveToDir = r'I:\Current\College'
    if category == "empty":
        for key in Media:
            if key in f:
                category = "Media"
                moveToDir = r'I:\Current\Media'
#------------------------------- MyLife Dir --------------------------------
    if category == "MyLife":
        if category == "MyLife":
            for key in Finances:
                if key in f:
                    category = "Finance"
                    moveToDir = r'I:\Current\MyLife\Finances'

        if category == "MyLife":
            for key in Health:
                if key in f:
                    category = "Health"
                    moveToDir = r'I:\Current\MyLife\Health'

        if category == "MyLife":
            for key in Home:
                if key in f:
                    category = "Home"
                    moveToDir = r'I:\Current\MyLife\Home'

        if category == "MyLife":
            for key in Travel:
                if key in f:
                    category = "Travel"
                    moveToDir = r'I:\Current\MyLife\Travel'
#------------------------------- Finance Dir ---------------------------------
    if category == "Finance":
        if category == "Finance":
            for key in Bills:
                if key in f:
                    category = "Bills"
                    moveToDir = r'I:\Current\MyLife\Finances\Bills'

        if category == "Finance":
            for key in Receipts:
                if key in f:
                    category = "Receipts"
                    moveToDir = r'I:\Current\MyLife\Finances\Receipts'

        if category == "Finance":
            for key in Tax:
                if key in f:
                    category = "Taxes"
                    moveToDir = r'I:\Current\MyLife\Finances\Taxes'
#---------------------------------College--------------------------------------
    if category == "College":
        if category == "College":
            for key in CS3343:
                if key in f:
                    category = "CS3343"
                    moveToDir = r'I:\Current\College\Fall\CS3343'

        if category == "College":
            for key in CS3733:
                if key in f:
                    category = "CS3733"
                    moveToDir = r'I:\Current\College\Fall\CS3733'

        if category == "College":
            for key in CS3773:
                if key in f:
                    category = "CS3773"
                    moveToDir = r'I:\Current\College\Fall\CS3773'

        if category == "College":
            for key in CS3853:
                if key in f:
                    category = "CS3853"
                    moveToDir = r'I:\Current\College\Fall\CS3853'
#-------------------------College SubDirs---------------------------------------
    if category == "CS3343" or category == "CS3733" or category == "CS3773" or category == "CS3853":
        for key in HW:
            if key in f:
                category = "HW"
                moveToDir = moveToDir + r'\HW'

        if category != "HW":
            for key in Quiz:
                if key in f:
                    category = "Quiz"
                    moveToDir = moveToDir + r'\Quiz'

        if category != "HW" and category != "Quiz":
            for key in Project:
                if key in f:
                    category = "Project"
                    moveToDir = moveToDir + r'\Projects'

        if category != "HW" and category != "Quiz" and category != "Project":
            for key in Labs:
                if key in f:
                    category = "Labs"
                    moveToDir = moveToDir + r'\Labs'
#------------------------- Media ----------------------------------------------
    if category == "Media":
        if category == "Media":
            for key in Photo:
                if key in f:
                    category = "Photo"
                    moveToDir = r'I:\Current\Media\Photo'

        if category == "Media":
            for key in Video:
                if key in f:
                    category = "Video"
                    moveToDir = r'I:\Current\Media\Video'

        if category == "Media":
            for key in docs:
                if key in f:
                    category = "docs"
                    moveToDir = r'I:\Current\Media\Docs'

        if category == "Media":
            for key in Audio:
                if key in f:
                    category = "Audio"
                    moveToDir = r'I:\Current\Media\Audio'


    if os.path.isfile(f): # double check that it is a file

        if not os.path.exists(os.path.join(moveToDir, ntpath.basename(f))): # double check if the file already exists in the redirected dir.
            if moveToDir == r'I:\Current': # check to see if file was sorted into a category
                moveToDir = r'I:\Current\Unsorted' # if not then move to unsorted dir
            shutil.move(f, moveToDir) # move file from origin to new sorted dir tree
            print(f, "Moved to ", moveToDir, "\n") # outputting statement to indicate from where to where the file was moved if moved

    moveToDir = rootDomain # resetting info before next iteration
    category = "empty" # restting before next iteration

