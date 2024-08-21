import requests

def download_zip_file(url, output_filename):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(output_filename, 'wb') as file:
            file.write(response.content)
        print(f"File successfully downloaded as {output_filename}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=581526a7a6006e81ba76412e09bf841a4a5a1a06"
    output_filename = "corpCode.zip"
    download_zip_file(url, output_filename)
