import requests, os
url = 'http://localhost:5000'
def download_file(filename,download_folder=''):
    download_url=f'{url}/download/{filename}'
    response=requests.get(download_url)
    if response.status_code==200:
        file_path=os.path.join(download_folder,filename)
        with open(file_path,'wb') as f:
            f.write(response.content)
            print(f"file '{filename}' downloaded successfully to '{download_folder}'")
    else:
        print(f"Failed to download file'{filename}':{response.text}")

if __name__=='__main__':
    file_to_download="down.jpg"
    download_folder='resources'
    
download_file(file_to_download,download_folder)   
