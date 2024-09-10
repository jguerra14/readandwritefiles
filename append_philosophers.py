def main():
    #open a file named philosophers.txt
    outfile = open('philosophers.txt', 'w')

    # Write our name to the bottom of the file
    outfile.write('Jeremy Guerra')

    #close the file
    outfile.close()

#call the main function
main()