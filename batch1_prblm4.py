#/*Write a python program to accept two filenames as command line arguments. Then copy contents of one file into another file adding line number to the beginning of each line and length of the line at the end of each line. Incorporate validation checks wherever applicable. 



import sys

def copy_file_with_line_numbers(input_file, output_file):
    try:
        #open input file in read mode
        with open(input_file,"r") as f:
            lines =f.readlines()

        #open output file in write mode
        with open(output_file,"w") as f:
            for i,line in enumerate(lines, start=1):
                #add line number at the beginning of each line
                line_with_number = f"{i}: {line.strip()}"
                #add length of the line at the end of each line
                line_with_number_and_length = f"{line_with_number} ({len(line)})\n"
                f.write(line_with_number_and_length)

        print(f"Contents of {input_file} copied to {output_file} with line number and length of lines..")

    except FileNotFoundError:
        print("File not found. please provide valid filename..")
    except Exception as e:
        print(f"an error occured: {e}")


if __name__=="__main__":
    #check if two filenames are provided as command line arguments
    if len(sys.argv)!=3:
        print("Usage: python program.py input_file output_file")

    else:
        input_file=sys.argv[1]
        output_file = sys.argv[2]
        copy_file_with_line_numbers(input_file, output_file)
