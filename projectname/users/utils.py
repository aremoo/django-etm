def parse_employee_data(file_path):
    problematic_lines = []
    with open(file_path, 'r') as file:
        content = file.read()

    user_blocks = content.split('\n\n')
    users_data = []

    for block in user_blocks:
        data = {}
        lines = block.split('\n') 
        try:
            data['user_name'] = lines[0].split(': ')[1].strip()
            data['employee_id'] = lines[1].split(': ')[1].strip()
            data['wage'] = float(lines[2].split(': ')[1].strip())
            data['vacation_balance'] = float(lines[3].split(': ')[1].strip())
            data['total_hours'] = float(lines[4].split(': ')[1].strip())
            data['reg_hours_pay'] = float(lines[5].split(': ')[1].strip())
            data['missed_hours_pay'] = float(lines[6].split(': ')[1].strip())
            # Use a loop for missed_dates to catch problematic lines
            missed_dates_list = []
            for line in lines[7:]:
                split_line = line.split(': ')
                if len(split_line) > 1:
                    missed_dates_list.append(split_line[1].strip())
                else:
                    # If you still want to keep track of problematic lines:
                    problematic_lines.append(line)   
            data['missed_dates'] = ', '.join(missed_dates_list)
            users_data.append(data) 
            
        except IndexError as e:
            print(f"Error processing block:\n{block}\nError: {str(e)}")
            
        except Exception as e:
            print(f"General error processing block:\n{block}\nError: {str(e)}")

    return users_data
