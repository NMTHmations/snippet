import sys
import os

def json_creator(fp, fpr, description, tab):
    fpr.write("\""+description+"\": {\n")
    print("\""+description+"\": {")
    fpr.write("    \"prefix\": \"{}\",\n".format(tab))
    print("    \"prefix\": \"{}\",".format(tab))
    fpr.write("    \"body\": [\n")
    print("    \"body\": [")
    for i in fp:
        string = str()
        if i[-1] == '\n':
            i = i[:-1]
            length = len(i)
            for j in range(length):
                if i[j] == '"':
                    string = string + '\\'
                    string = string + '\"'
                else:
                    string = string + i[j]
        fpr.write("        \"{}\"\n".format(string))
        print("        \"{}\"".format(string))
    fpr.write("    ],\n")
    print("    ],")
    fpr.write("    \"description\": \"{}\"\n".format(description))
    print("    \"description\": \"{}\"".format(description))
    fpr.write("}\n")
    print("}")

def main(arg):
    if len(arg) != 5:
        print("Syntax: python3 snippet.py [description] [tab trigger] [file] [JSON file name]")
        return False
    filename = arg[3]
    if os.path.exists(filename) == False:
        print('File does not exist!')
        return False
    fp = open(filename,"rt")
    json_name = arg[4]
    fpr = open(json_name,"wt")
    description = arg[1]
    tab = arg[2]
    json_creator(fp,fpr,description,tab)
    fp.close
    fpr.close
    return True

if __name__ == "__main__":
    arg = sys.argv
    main(arg)