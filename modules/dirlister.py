import os 

def run(**args):
    print "[*] In dirlister module"
    files = str(os.listdir("."))
    mod_description = "Results for dirLister module:\n\n"
    return mod_description + files
