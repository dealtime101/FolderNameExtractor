Directory Listing Tool
Project Description

This Directory Listing Tool is a Python script designed to help users list all subdirectories within a specified directory and save the names to a text file. This tool is useful for auditing directory structures, backup logs, or simply organizing and documenting the contents of your storage.
Key Features

    List Subdirectories: Easily list all subdirectories in a given directory.
    Save to Text File: Automatically save the list of directory names to a text file for further processing or documentation.
    Customizable Save Location: Configure the save location for the output file through the script.

Getting Started
Prerequisites

Ensure you have Python installed on your system. This script is compatible with Python 3.x. You can download Python from python.org.
Installation

Clone this repository to your local machine to get started with the Directory Listing Tool:

bash

git clone https://github.com/yourusername/directory-listing-tool.git
cd directory-listing-tool

Usage

Run the script from the command line, providing the path of the directory you want to analyze:

bash

python directory_listing.py

Follow the prompts to enter the directory path. The script will generate a file named directory_names.txt in the specified output location, containing the names of all subdirectories.
Configuration

To change the default save location of the output file, modify the save_folder variable in the script:

python

save_folder = "desired/path/to/save/output"

Ensure this path is accessible and writable on your system.
Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

    Fork the Project
    Create your Feature Branch (git checkout -b feature/AmazingFeature)
    Commit your Changes (git commit -m 'Add some AmazingFeature')
    Push to the Branch (git push origin feature/AmazingFeature)
    Open a Pull Request

License

Distributed under the MIT License. See LICENSE for more information.
Contact

Your Name - your-email@example.com

Project Link: https://github.com/yourusername/directory-listing-tool
