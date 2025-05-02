import xml.etree.ElementTree as ET

# specify the path to your concatenated XML file
xml_file = "Data/ipg200107.xml"

# parse the concatenated XML file
with open(xml_file, "r", encoding="utf-8") as f:
    xml_string = f.read()
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

    # print the full text
    print(full_text)