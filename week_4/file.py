def read_and_write_file():
  
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write the modified content: ")

    try:
      
        with open(input_filename, 'r') as file:
            content = file.read()  

    
        modified_content = content.upper()

  
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"File content has been successfully modified and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_write_file()
