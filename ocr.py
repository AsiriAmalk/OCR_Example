import pytesseract as tess
import datetime
import os
import cv2

input_path = "USABLE_IMAGES_TEST/"
logfile_path = "LOGFILE/"
output_path = "OUTPUTS/"

imglist = os.listdir(input_path)
imageList = [(lambda x: input_path +x)(x) for x in imglist]

try:
    os.mkdir(output_path)
    print("Output File: {:s} has been created".format(output_path))
except FileExistsError:
    print("File Already Exists...!")

try:
    os.mkdir(logfile_path)
    print("Output File: {:s} has been created".format(logfile_path))
except FileExistsError:
    print("File Already Exists...!")

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


logfile = open(logfile_path + "logfile.txt", 'w+')
logfile.write("Name,path,date,time\n")
all_list = []

print("################# OCR STARTED #######################################")

for i in range(len(imageList)):

    word_list = []
    name = imglist[i].split(".")[0]
    serial_number = "Serial Number = Not Recognized!"
    img = cv2.imread(imageList[i])

    img = cv2.resize(img, None, fx=0.5, fy=0.5)
    # converting into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Putting the threshold
    adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
    # config="--psm 3"
    text = tess.image_to_string(adaptive_threshold, lang='eng')  # config=config

    #     text = tess.image_to_string(img)
    t = text.replace('\r', ' ')
    text_line = t.splitlines()

    start = 100
    end = None

    for line in range(len(text_line)):
        word = text_line[line]
        word_split = word.split("-")

        if "EASTING" in word or "LINE" in word or "NORTHING" in word or "DIST" in word:
            if start > line:
                start = line

        if "AREA=" in word or "AREA =" in word:
            end = line
            REAL = word.split(" ")[0:5]
            separator = ' '
            separator.join(REAL)
            word_list.append(separator.join(REAL))

            if start == None:
                for te in range(len(text_line)):
                    try:
                        if len(str(int(float(text_line[te].split(" ")[0])))) == 6:
                            #                             word_list.append(text_line[te:line])
                            start = te
                            break
                    except:
                        continue

        if len(word_split) == 5:
            s_split = word.split("-")
            s_last = s_split[-1].split(" ")[0]
            serial_number = ""
            for s in s_split[:-1]:
                serial_number += s
                serial_number += "-"
            serial_number += s_last
            serial_number = "Serial Number = {:s}".format(serial_number)

    word_list.insert(0, serial_number)

    separator = '\r'
    #     separator.join(all_list[2][2:])
    if (start != 100) and (end != None):
        #         print(separator.join(text_line[start:end]))
        word_list.extend(text_line[start:end])
    #         print(start, " and ", end)
    separator = '\n'

    file_name = output_path + name + ".txt"
    path = os.path.abspath(file_name)

    time = datetime.datetime.now().strftime("%d%m%Y, %H:%M%p")

    logfile.write(name + "," + path + "," + time + "\n\n")

    file = open(file_name, 'w+')

    print("{:s} : {:d} out of {:d} created..".format(path, i + 1, len(imageList)))

    try:
        file.write(separator.join(word_list))
    except:
        file.write(word_list)
    #     file.write(separator.join(word_list))
    file.close()
    #     print(word_list)
    all_list.append(word_list)
logfile.close()

print("################# OCR END #######################################")