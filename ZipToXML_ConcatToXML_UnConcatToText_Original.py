import os
import zipfile
import xml.etree.ElementTree as ET

# Directory containing .zip files
zip_dir_path = r'C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\Full_Text_US\2023'



# Create an empty string to store the concatenated XML text
xml_text = ''

# Loop through all ZIP files in the directory
for file_name in os.listdir(zip_dir_path):
    if file_name.endswith('.zip'):

        # Open the ZIP file and extract all XML files to a temporary directory
        zip_path = os.path.join(zip_dir_path, file_name)
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            tmp_dir_path = '/tmp/xml_files'
            zip_file.extractall(tmp_dir_path)

        # Concatenate the text from all XML files
        for xml_file_name in os.listdir(tmp_dir_path):
            xml_path = os.path.join(tmp_dir_path, xml_file_name)
            with open(xml_path, 'r') as xml_file:
                xml_string = xml_file.read()
                xml_string = xml_string.replace('\n', '').replace('\r', '')
                xml_list = xml_string.split("<?xml ")

            # iterate over each individual XML document and extract its text
            for i, xml_str in enumerate(xml_list[1:]):
                xml_str = "<?xml " + xml_str.strip()

                """
                # save each individual XML document to a file
                xml_doc.write(f"output_{i}.xml")
                """

                xml_string = xml_str.replace('\n', '').replace('\r', '')
                root = ET.fromstring(xml_string)

                # iterate over all elements in the XML tree and extract their text
                full_text = ""
                for elem in root.iter():
                    if elem.text is not None:
                        full_text += elem.text.strip() + " "
                        print(full_text)
                xml_text += full_text




        # Delete the temporary directory and its contents
        for tmp_file_name in os.listdir(tmp_dir_path):
            tmp_file_path = os.path.join(tmp_dir_path, tmp_file_name)
            os.remove(tmp_file_path)
        os.rmdir(tmp_dir_path)
        # print(xml_text)

# Print the concatenated XML text
print(xml_text)