import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
import zipfile
from iteration_utilities import duplicates
##script used to extract zipped xml
##with zipfile.ZipFile(r"D:\PY\astra_export_xml.zip","r") as zip_ref:
##    zip_ref.extractall("D:\PY")



xml = "export_full.xml"
tree=ET.parse(xml)
root=tree.getroot()

def items():
    list1 = []
    for z in root.find("items"):
        list1.append({z.attrib["code"] : z.attrib["name"]})
    return list1

def spare_parts():
    spare_part_list = []
    for z in root.find("items"):
        for parts in z.findall("parts"):
            for part in parts:
                for item in part:
                    spare_part_list.append({item.attrib["name"] : part.attrib["name"] })
    return spare_part_list

while True:
    user = input("Enter total, product, spares or finished:  ")
    user = user.lower()
    if user.isalpha():
        if user == "total":
            print("Total number of products: {} items".format(len(items())))
            continue
        elif user == "product":
            print("list of product names: {}".format(items()))
        elif user == "spares":
            print("List of product names with spare parts: {}".format(spare_parts()))
        elif user == "finished":
            print("Thank you for using us, bye! :-)")
            break            
        else:
            print("Please use one of the given options")
    else:
        print("Please don't use digits")


