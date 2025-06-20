def blobularise():
    try:
        with open('round_filter.rs2f', 'r') as input_file:
            lines = input_file.readlines()

        processed_lines = []
        for line in lines:
            line = line.replace("icon = CurrentItem();", "")
            line = line.replace("fontType = 3;", "")
            line = line.replace("Round filter", "Round filter - Wub version")
            processed_lines.append(line)

        with open('round_filter_wubmode.rs2f', 'w') as output_file:
            output_file.writelines(processed_lines)
            
        print("blobularise success")
        
    except FileNotFoundError:
        print("Error: Input file 'round_filter.rs2f' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    blobularise()