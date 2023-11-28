def has_even_angle_brackets(line):
    count_open = line.count("<")
    count_close = line.count(">")
    
    if count_open == 0:
        return False
    if count_close == 0:
        return False
    
    if len(line) < 10:
        return False

    if count_open < 2 or count_close < 2:
        return False

    if count_open == count_close:
        return True
    

def get_lines_with_odd_brackets(file_path, output_file_path):
    suspicious_lines = []
    closed_lines = []

    with open(file_path, 'r',encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if not has_even_angle_brackets(line):
                suspicious_lines.append((line_number, line.strip()))
            else:
                closed_lines.append(line)

    # Save lines with even brackets to a new file
    with open(output_file_path, 'w',encoding='utf-8') as output_file:
        output_file.writelines(closed_lines)

    return suspicious_lines

input_file_path = 'clean_papelerascaninas_data2.nt'  # Replace with the path to your input file
output_file_path = 'clean_papelerascaninas_data3.nt'  # Replace with the desired output file path
result = get_lines_with_odd_brackets(input_file_path, output_file_path)

for line_number, line in result:
    print(f"Line {line_number}: {line}")

print(f"Lines with even brackets saved to {output_file_path}")
