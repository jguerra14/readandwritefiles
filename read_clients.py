# Example In-class program
# This program reads and displays the contents
#  of the clients.txt file
def main():
    # Open a file called 'clients.txt' in read form
    infile = open('clients.txt', 'r')

    # Set counter variable equal to one
    count = 1

    # Read and iterate through each line in the file
    #  and increment count for each record and print
    #  each client out
    for line in infile:
        #linex = infile.readline()
        #count += 1
        #print(count)
        #print('. ' + linex)
        
        print(f"{count}. {line.rstrip('\n')}")
        count += 1

    print()
    print(f"Total number of clients: {count}")

# Call the main method
main()