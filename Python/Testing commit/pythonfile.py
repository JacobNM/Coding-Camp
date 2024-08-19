import os
import datetime

def find_old_files(folder_path):
    current_time = datetime.datetime.now()
    ten_days_ago = current_time - datetime.timedelta(days=10)
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if file_modified_time < ten_days_ago:
                print(f"{file_path} is more than 10 days old.")

# Replace 'folder_path' with the path to the folder you want to search
folder_path = '/path/to/folder'
find_old_files(folder_path)