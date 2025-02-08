import os

def scan_folder(folder_name: str):
    scanned_files = []
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            if file.endswith(".py"):
                if file == "__init__.py":
                    continue
                scanned_files.append(file.strip(".py"))


    return scanned_files

if __name__ == "__main__":
    print(scan_folder("src/commands/implementations/"))
