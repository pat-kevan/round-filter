def process_file():
    try:
        # Open the input file for reading
        with open('round_filter.rs2f', 'r') as input_file:
            # Read all lines into a list
            lines = input_file.readlines()

        # Filter out the unwanted lines
        filtered_lines = [line for line in lines 
                         if "icon = CurrentItem();" not in line 
                         and "fontType = 3;" not in line]

        # Write the filtered content to the output file
        with open('round_filter_wubmodetest.rs2f', 'w') as output_file:
            output_file.writelines(filtered_lines)
            
        print("File processed successfully!")
        
    except FileNotFoundError:
        print("Error: Input file 'round_filter.rs2f' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    process_file()