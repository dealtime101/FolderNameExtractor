import os

save_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')


def list_directories(path):
    if not os.path.isdir(path):
        print(f"The specified path ({path}) is not a directory.")
        return

    directory_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

    output_file_path = os.path.join(save_folder, "directory_names.txt")

    with open(output_file_path, 'w') as file:
        for directory in directory_names:
            file.write(directory + '\n')

    print(f"Folder names were saved in {output_file_path}")
    continue_prompt = input(f"Do you want to open the file? Y/N")
    if continue_prompt == "Y" or "y":
        print("Opening directory_names.txt")
    else:
        return


if __name__ == "__main__":
    user_path = input("Enter the folder path to list its subfolders: ")
    list_directories(user_path)
