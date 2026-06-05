def merge_employee_data(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        print("Both inputs must be dictionaries.")
        return
    dict1.update(dict2)
    print("Merged Employee Data:", dict1)

hr_data = {"Alice": "HR", "Bob": "IT"}
new_hires = {"Charlie": "Sales", "Alice": "Senior HR"} # Overwrites Alice
merge_employee_data(hr_data, new_hires)