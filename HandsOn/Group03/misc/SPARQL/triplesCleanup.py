def has_even_angle_brackets(line):
    count_open = line.count("<")
    count_close = line.count(">")
    return count_open == count_close

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

input_file_path = fr"C:\Universidad2_año\Trabajo_wed_Semantica\Curso2023-2024-DataScience\HandsOn\Group03\misc\FuentesCaninas202310\Assigment4_FuentesCaninas-AndreaMejia\rdf\papelerascaninas_data.nt"  # Replace with the path to your input file
output_file_path = fr'C:\Universidad2_año\Trabajo_wed_Semantica\Curso2023-2024-DataScience\HandsOn\Group03\misc\FuentesCaninas202310\Assigment4_FuentesCaninas-AndreaMejia\rdf\papelerascaninas_data_clean.nt'  # Replace with the desired output file path
result = get_lines_with_odd_brackets(input_file_path, output_file_path)

for line_number, line in result:
    print(f"Line {line_number}: {line}")

print(f"Lines with even brackets saved to {output_file_path}")
