def main():
    # File creation and writing
    try:
        # Open a new file in write mode
        with open('my_file.txt', 'w') as file:
            # Write three lines of text to the file
            file.write("Hello, this is the first line.\n")
            file.write("Here is the second line with a number: 12345\n")
            file.write("And this is the third line.\n")
        
        print("File created and data written successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File write operation completed.")

    # File reading and displaying
    try:
        # Open the file in read mode
        with open('my_file.txt', 'r') as file:
            # Read the content of the file
            content = file.read()
            print("\nContent of 'my_file.txt':")
            print(content)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File read operation completed.")

    # File appending
    try:
        # Open the file in append mode
        with open('my_file.txt', 'a') as file:
            # Append three additional lines of text
            file.write("Appending the fourth line.\n")
            file.write("Appending the fifth line with another number: 67890\n")
            file.write("Appending the sixth and final line.\n")
        
        print("Data appended successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File append operation completed.")

if __name__ == "__main__":
    main()
