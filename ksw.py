import os
import requests

base_urls = [
    "https://faponic.com/data/c/u/curvygirl/1000/curvygirl_",
    "https://faponic.com/data/k/o/kobaebeefboo/1000/kobaebeefboo_",
    "https://faponic.com/data/s/e/sejinming/1000/sejinming_",
    "https://faponic.com/data/r/e/reilin/1000/reilin_",
    "https://faponic.com/data/n/o/norafawn/2000/norafawn_"
]
photo_number = 1

# create a directory for the downloaded images
if not os.path.exists("photos"):
    os.mkdir("photos")
    print("Created directory: photos")

# loop through each base URL until the maximum photo number is reached
for base_url in base_urls:
    # extract the directory name from the base URL
    dirname = os.path.basename(base_url.rstrip('/'))
    # create a directory with the dirname
    dirname_path = os.path.join("photos", dirname)
    if not os.path.exists(dirname_path):
        os.mkdir(dirname_path)
        print(f"Created directory: {dirname_path}")
    
    while True:
        # create the URL for the current photo
        photo_url = base_url + f"{photo_number:04}.jpg"
        
        # create the filename for the current photo
        filename = os.path.join(dirname_path, f"name_{photo_number:04}.jpg")
        
        # simulate a web browser by setting the User-Agent header
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        
        # download the photo and save it to disk using Requests library
        response = requests.get(photo_url, headers=headers)
        if response.status_code == 404:
            print(f"Reached the end of the photos for {base_url}. Downloaded {photo_number-1} photos.")
            photo_number = 1
            break
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
        
        # increment the photo number
        photo_number += 1
