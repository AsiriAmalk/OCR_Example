import pdf2image
import os
from pdf2image import convert_from_path
import cv2

input_path = "./Image test/"
usable_image_path = "USABLE_IMAGES_TEST/"

try:
    os.mkdir(usable_image_path)
    print("Output File: {:s} has been created".format(usable_image_path))
except FileExistsError:
    print("File Already Exists...!")


imglist = os.listdir(input_path)
imageList = [(lambda x: input_path +x)(x) for x in imglist]


# convert pdf to png
def save_iamges(imglist, imageList, output_path):
    try:
        os.mkdir(output_path)
        print("Usable Images Output Folder: {:s} has been created\n".format(output_path))
    except FileExistsError:
        print("Folder Already Exists...!\n")

    pdf_count = 0
    img_count = 0
    falt_count = 0

    for i in range(len(imageList)):
        im_name = imglist[i]

        try:
            if imageList[i][-3:] == 'pdf':
                pdf_name = imglist[i][:-3] + "png"
                pdf_path = imageList[i]
                #         print(pdf_name)
                pages = convert_from_path(pdf_path)
                for page in pages:
                    page.save(output_path + pdf_name, "png")
                    pdf_count += 1
                print("Saved and converted {:s}  to {:s}".format(imglist[i], pdf_name))
                img_count +=1

            else:
                img = cv2.imread(imageList[i])
                print("Saved {:s}".format(im_name))
                cv2.imwrite(output_path + im_name, img)
                img_count += 1
        except:
            falt_count += 1
            print("{:s} is not a image or a pdf".format(imglist[i]))

    print("\n##############################################")
    print("Total {:d} images saved".format(img_count))
    print("Total {:d} pdf converted to image".format(pdf_count))
    print("Total {:d} is not an image or pdf".format(falt_count))
    print("################################################")

    imglist = os.listdir(output_path)
    imageList = [(lambda x: input_path + x)(x) for x in imglist]

    return imglist, imageList

save_iamges(imglist, imageList, output_path=usable_image_path)