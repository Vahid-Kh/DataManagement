"""
Extracting text from zipped Concatenated XML files

    1- Takes a folder containing zip file (Loops through a list of folders)
    2- Opens zip in temporary file
    3- Opens Concatenated XML & make them UnConcatenated XML
    4- Strips tags fromm XML file and turns the text

"""


import os
import zipfile
import xml.etree.ElementTree as ET


# Directory containing .zip files
zip_dir_path = r'C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\Full_Text_US'
outputFileName = r'C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\Text'

years= [
    # "2023",
    "2022a",
    # "2021",
    # "2020",
    # "2019",
    # "2018",
    # "2017",
    # "2016",
    # "2015",
    # "2014",
    # "2013",
    # "2012",
    # "2011",
    # "2010",
    # "2009",
    # "2008",
    # "2007",
    # "2006",
    # "2005",
    # "2004",
    # "2003",
    # "2002",
    # "2001",
    # "2000",
    ]

for y in range(len(years)):
    print("_______________YEAR :  ", years[y], "_________________-")
    zip_dir_path+="\\"+ years[y] + "\\"
    print("Zip file currently converting to text : ", zip_dir_path)
    # Create an empty string to store the concatenated XML text
    xml_text = ''

    # Loop through all ZIP files in the directory
    for file_name in os.listdir(zip_dir_path):
        if file_name.endswith('.zip'):
            # Open the ZIP file and extract all XML files to a temporary directory
            zip_path = os.path.join(zip_dir_path, file_name)
            print(zip_path)
            print(outputFileName+ "\\" + str(zip_dir_path[-5:]))

            with zipfile.ZipFile(zip_path, 'r') as zip_file:
                tmp_dir_path = '/tmp/xml_files/'+ years[y] + "\\"
                zip_file.extractall(tmp_dir_path)

            # Concatenate the text from all XML files
            for xml_file_name in os.listdir(tmp_dir_path):
                xml_path = os.path.join(tmp_dir_path, xml_file_name)
                print(xml_path)

                with open(xml_path, 'r') as xml_file:
                    xml_string = xml_file.read()
                    xml_string = xml_string.replace('\n', '').replace('\r', '')
                    xml_list = xml_string.split("<?xml ")

                # iterate over each individual XML document and extract its text
                for i, xml_str in enumerate(xml_list[1:]):
                    xml_str = "<?xml " + xml_str.strip()
                    """# save each individual XML document to a file
                    xml_doc.write(f"output_{i}.xml")
                    """
                    xml_string = xml_str.replace('\n', '').replace('\r', '')

                    try:
                        root = ET.fromstring(xml_string)
                        # iterate over all elements in the XML tree and extract their text
                        full_text = ""
                        for elem in root.iter():
                            if elem.text is not None:
                                full_text += elem.text.strip() + " "

                        xml_text += full_text
                        if i % 500 == 0:
                            print("# of XML : ", '{:>10}'.format(i),
                                  " | 1st 50 Char :", '{:>51}'.format(str(full_text[:50])),)
                    except:
                        if i % 500 == 0:
                            print("# of XML : ", '{:>10}'.format(i), "!!!An exception has occurred!!!")

            # Delete the temporary directory and its contents
            for tmp_file_name in os.listdir(tmp_dir_path):
                tmp_file_path = os.path.join(tmp_dir_path, tmp_file_name)
                os.remove(tmp_file_path)
            os.rmdir(tmp_dir_path)
            # print(xml_text)

        text = ''.join([i if ord(i) < 128 else ' ' for i in xml_text])
        with open(outputFileName+ "\\" + str(zip_dir_path[-5:-1]) + str(file_name) + '.txt', "w", encoding="utf-8") as text_file:
            text_file.write(text)

        print("TXT File saved with name: ", str(outputFileName)+ "\\" + str(zip_dir_path[-5:-1]) + str(file_name[-4:]) + '.txt')