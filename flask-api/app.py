from flask import Flask, jsonify, Request, request
from pycrate_asn1compile import execute
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)


@app.route('/encode', methods=['POST'])
def encode_text():
    '''
    This function encodes the values into the python structures.
    Rules:
    For encoding the values into the python data structures
    and getting the ber encoding, the following rules need
    to be followed while inputting the values into the textbox
    in the play ground-
    1. If no specific variable you want to encode from the class
       simply write a dictionary with all the key value pairs of
       the asn class value variables.
    2. If a specific variable from the class you want to set value
       and encode it then write that varible in the same case as
       written in class then put a "=" and write the dictionary with
       key value pairs stating the key as the sub variable and value
       as the value of the sub variable

    returns: dictionary with the ber encoding
    '''
    output_dict={}
    values=request.data.decode()
    variable=""
    if "=" in values:
        variable=values.split("=")[0].split()[0]
        values= eval(values.split("=")[0].split()[1])
    else:
        values= eval(values)
    import out
    output_file=open("out.py", "r")
    class_find = output_file.read()
    class_find=class_find.split("\n")
    final_name=""
    for i in class_find:
        class_name=i.split()
        if "class" in class_name:
            final_name=class_name[1].split(":")[0]
            break
    encoding=getattr(out, final_name)
    if variable is not "":
        encoding=getattr(encoding,variable)
    encoding.set_val(values)
    ber_encoding=str(encoding.to_ber())
    output_dict["ber_encoding"]=ber_encoding
    jsonify(output_dict)


@app.route('/structures', methods=['POST'])
def get_structures():
    '''
    This function is for getting the python get_structures.

    returns:a dictionary with the python structure.
    '''
    send_dict = {}
    text = eval(request.data.decode())
    text = text["asn_text"]
    text = text.split("\n")
    file = open("test.asn1", "w")
    for i in text:
        file.write(i)
        file.write("\n")
    file.close()
    execute()
    file_new = open("out.py", "r")
    output = file_new.read()
    send_dict["output"] = output
    os.remove("test.asn1")
    return jsonify(send_dict)


@app.route('/decode', methods=['POST'])
def decode_text():
    print("This is the function which decodes the python structures.")


app.run(host='0.0.0.0', port=8658, debug=True)
