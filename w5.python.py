def read_and_reverse_file():
    # Ask user for input filename
    input_file = input("📝 Enter the name of the file to read: ")

    try:
        # Try to open the file in read mode
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Modify the contents: reverse each line
        reversed_lines = [line[::-1] for line in lines]

        # Define output file name
        output_file = "reversed_" + input_file

        # Write modified content to a new file
        with open(output_file, 'w') as file:
            file.writelines(reversed_lines)

        print(f"✅ Reversed content written to '{output_file}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: The file cannot be read.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# Run the function
read_and_reverse_file()
