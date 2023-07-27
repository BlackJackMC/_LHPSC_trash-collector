import requests
import os

def _fetch_data(owner, repo_name, path, access_token=None):
    base_url = "https://api.github.com/repos"
    url = f"{base_url}/{owner}/{repo_name}/contents/{path}"
    
    headers = {}
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        contents = response.json()
        return contents
    else:
        raise Exception(f"Failed to fetch contents. Status code: {response.status_code}, Error: {response.text}")

def _save_data(contents, local_folder, access_token=None):
    headers = {}
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    
    os.makedirs(local_folder, exist_ok=True)
    for item in contents:
        file_name = item["name"]
        file_download_url = item["download_url"]
        local_file_path = os.path.join(local_folder, file_name)
        file_response = requests.get(file_download_url, headers=headers)
        if file_response.status_code == 200:
            with open(local_file_path, "wb") as file:
                file.write(file_response.content)
        else:
            raise Exception(f"Failed to download {file_name}. Status code: {file_response.status_code}")


def download_map(owner, repo_name, path, local_folder):
    try:
        data = _fetch_data(owner, repo_name, path)
        _save_data(data, local_folder)
    except:
        raise Exception(f"Failed to update map")
    else:
        return True

def main():
    print("A module to download folder from github (Use in this repo only)")
    print("Please import from another file to use")

if __name__ == "__main__":
    main()