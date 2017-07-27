import os 

def run(*args):
    print "[*] In dirlister module"
    if len(args) == 0:
        files = str(os.listdir("."))
    elif len(args) == 1:
        files = str(os.listdir(args[0]))
    else:
        print "[*] Too many arguments in dirlister module... Quitting"
        sys.exit(1)
        
    mod_description = "Results for dirLister module:\n\n"
    return mod_description + files
