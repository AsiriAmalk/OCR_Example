# OCR text identifier 

## * User needes install `Tesseract` and setup `Poppler` manually to the computer

## ** Create a folder called `images` and put all your images into the folder before run below

# Setup Poppler
### Windows
#### Windows users will have to install poppler for Windows, then add the bin/ folder to PATH.
http://blog.alivate.com.au/poppler-windows/
 
### Mac
#### Mac users will have to install poppler for Mac.
http://macappstore.org/poppler/


# Install Pytesseract

## Download and install Tesseract to your computer
* https://github.com/tesseract-ocr/tesseract/wiki
* pip install pytesseract

# Copy the installation path as shown as below
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Install all dependencies

#### ✔ OpenCV
#### ✔ Numpy
#### ✔ Pdf2Image
#### ✔ Pillow
####  ✔ Pytesseract

# Use `pip install -r requirements.txt`

# run `python image_update.py`

# run `ocr.py`

# Results will be `OUTPUT` and  `LOGFILE` folders