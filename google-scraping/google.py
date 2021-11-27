from google_images_download import google_images_download

# class instantiation
response = google_images_download.googleimagesdownload()

# download memes from 2000 to 2021
for i in range(0, 22):
    year = 2000 + i
    # creating list of arguments
    arguments = {"keywords": str(year) + " memes",
                 "limit": 20, "print_urls": True, "format": "jpg"}

    # passing the arguments to the function
    paths = response.download(arguments)

    # printing absolute paths of the downloaded images
    print(paths)