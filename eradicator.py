import os

def delete_files_with_extension(root_directory, extension):
    try:
        print("\n")
        for root, dirs, files in os.walk(root_directory):
            for filename in files:
                if filename.endswith(extension):
                    file_path = os.path.join(root, filename)
                    os.remove(file_path)
                    print(f"Deleted: {filename} + {extension}")
        print(f"\nAll files with the '{extension}' extension have been deleted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    current_directory = os.getcwd()  
    extension_to_delete = input("\nEnter extension to remove: ")
    is_sure = input(f"\nAre you sure you want to remove everything with {extension_to_delete}\n"
                    "[in this directoru as well as subdirectories] (Y/N): ").upper()
    if(is_sure == "Y"):
        delete_files_with_extension(current_directory, extension_to_delete)


if __name__ == "__main__":
    main()
    Continue = input("Delete more? (Y/N): ").upper()
    if(Continue == "Y"):
        main()    
    exit()