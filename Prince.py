import os, sys, time, subprocess

def requirements():
    modules = ['requests', 'bs4', 'faker', 'fake_email']
    for mod in modules:
        try:
            __import__(mod)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", mod], stdout=subprocess.DEVNULL)
            time.sleep(1)
            os.execl(sys.executable, sys.executable, *sys.argv)

def loader():
    os.system('clear')
    try:
        import prince2_0_enc
        prince2_0_enc.akash()
    except ImportError:
        print("\n\033[1;91m[!] Error: prince2_0_enc.cpython-312.so NOT FOUND!")
        sys.exit()
    except Exception as e:
        print(f"\n\033[1;91m[!] Error: {e}\033[0m")
        sys.exit()

if __name__ == "__main__":
    requirements()
    loader()
