# Pearson PDF Downloader
Pearson PDF Downloader is a utility to download ebook from [https://elibrary.in.pearson.com/](https://elibrary.in.pearson.com/) considering you have the `book_id`.

## Installation
Install all the requirements

    pip install -r requirements.txt

## Usage
The steps to get pearson `book_id` is shown below:
 1. Login to https://elibrary.in.pearson.com/ with your credentials.
 2. Search and open the book you want to download
 3. Get `book_id` and `page_count` using inspect element
 ![enter image description here](https://raw.githubusercontent.com/Bishalsarang/Pearson-PDF-Downloader/master/assets/sc0.gif?token=ACT7E5ZG3GLMCRWKTUIY2Z26SL2F6)
 After getting book_id and page_count you can download the pdf running.
     python pdl.py
     ![enter image description here](https://raw.githubusercontent.com/Bishalsarang/Pearson-PDF-Downloader/master/assets/sc1.gif?token=ACT7E5ZTVGFCD7HLXBK25OS6SL2IY)
The ebooks are downloaded as pdf.

## TODOS:
Right now, I'm only able to download image as pdfs which is larger in size. I was able to grab the zip file that contains the true pdf for the book which is unfortunately password protected.

 - [x] Concurrency
 - [x] Convert images to pdf
 - [ ] Downloading true pdf

