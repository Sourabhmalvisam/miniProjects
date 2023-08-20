import os

def main():
    i = 0  # Initialize a counter for generating new filenames
    path = "C:/Users/Sourabh/Desktop/Rename Test/"  # Specify the directory path

    # Iterate through each filename in the directory
    for filename in os.listdir(path):
        new_file_name = "img" + str(i) + ".jpg"  # Generate a new filename
        my_source = path + filename  # Source path of the file
        my_dest = path + new_file_name  # Destination path with the new filename

        # Rename the file by moving it to the destination path
        os.rename(my_source, my_dest)
        
        i += 1  # Increment the counter for the next filename

if __name__ == '__main__':
    main()  # Call the main function to initiate the renaming process
