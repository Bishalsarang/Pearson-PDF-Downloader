import os
import requests
import argparse
import glob
import img2pdf
from multiprocessing.pool import ThreadPool


class Downloader(object):
    def __init__(self, book_id, page_count, download_dir):
        self.book_id = book_id
        self.page_count = page_count
        self.download_dir = download_dir

        self.urls = ((f"{self.download_dir}/{i}.png",
                 f'https://d38l3k3yaet8r2.cloudfront.net/resources/products/epubs/generated/'
                 f'{self.book_id }/foxit-assets/pages/page{i}?password=&accessToken=null&formMode=true')
                for i in range(self.page_count))

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir )

    def fetch_url(self, entry):
        path, uri = entry
        if not os.path.exists(path):
            r = requests.get(uri, stream=True)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
        return path

    def save_images(self):
        results = ThreadPool(8).imap_unordered(self.fetch_url, self.urls)
        for path in results:
            print(path)
        print("Downloading Images Completed")

    def save_pdf(self):
        with open(f"{self.download_dir}/{self.download_dir}.pdf", "wb") as f:
            f.write(img2pdf.convert(glob.glob(f"{self.download_dir}/*.png")))
        print("Saved pdf successfully")


def main():
    page_count = int(input("Enter total pages: "))
    book_id = input("Enter book id: ")
    download_dir = input("Enter Download path: ")

    downloader = Downloader(book_id, page_count, download_dir)
    downloader.save_images()
    downloader.save_pdf()

if __name__ == "__main__":
    main()

