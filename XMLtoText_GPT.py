import os
import zipfile
import xml.etree.ElementTree as ET
# Directory containing .zip files
zip_dir_path = r'C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\Full_Text_US\2023'


# Loop through all zip files in the directory
for file in os.listdir(zip_dir_path):
    if file.endswith('.zip'):
        # Extract all files in the zip file
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall()

        # Concatenate all XML files and strip tags
        full_text = ''
        for xml_file in os.listdir():
            if xml_file.endswith('.xml'):
                with open(xml_file, 'r') as f:
                    xml_data = f.read()
                    root = ET.fromstring(xml_data)
                    full_text += ET.tostring(root, encoding='unicode', method='text')

        # Print the full text with tags stripped
        print(ET.fromstring(full_text).text)
