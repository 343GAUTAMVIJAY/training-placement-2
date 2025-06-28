import shutil
import os

folder = 'source_folder'  # Replace with your folder
output = 'backup.zip'
shutil.make_archive(output.replace('.zip', ''), 'zip', folder)
print(f"Backup created: {output}")