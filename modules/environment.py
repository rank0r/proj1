import os

def run(**args):
    print "[*] In environment module"
    environ = str(os.environ)
    mod_description = "Results for environment module\n\n"
    return mod_description + environ
