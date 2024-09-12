# Example:
# This program reads and displays the contents
#  of the philosopher.txt file
def main():
    # Open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    # Read the file's contents
    # Can either rstrip inside of the read statement or later
    #file_contents = infile.read()
    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')

    # Print the data that was read into memory
    #print(file_contents)
    print(line1)
    print(line2)
    print(line3)

# Call the main function
main()