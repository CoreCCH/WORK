import pandas as pd
import copy



data = {}
list_data = []

def excel_file_read(file_name: str, sheet_name: str):
    # 讀取 Excel 文件
    return pd.read_excel(file_name, sheet_name)

#get KEY array
def get_key_array(data: dict):
    unique_items = set()
    # Extract and add items from 'SMT'
    for key in data.values():
        for item in key:
            unique_items.update(item.keys())

    # Convert the set to a list
    unique_list = list(unique_items)
    return unique_list

#return capacity
def add_capacity(df2):
    return_dict = {}
    X7R_list = []
    X5R_list = []
    NPO_list = []


    X7R_column_values_code = df2.iloc[:, 7]
    X5R_column_values_code = df2.iloc[:, 9]
    NPO_column_values_code = df2.iloc[:, 11]

    for index in range(X7R_column_values_code.size):
        if (X7R_column_values_code[index] != "4.編號"  and pd.notna(X7R_column_values_code[index])):
            X7R_list.append(str(X7R_column_values_code[index]))
            X5R_list.append(X5R_column_values_code[index])
            NPO_list.append(NPO_column_values_code[index])

    return_dict.update({'X7R':X7R_list})
    return_dict.update({'X5R':X5R_list})
    return_dict.update({'NPO':NPO_list})

    return return_dict

#return array
def excel_list_read(df):
    return_value = []

    column_values = df.iloc[:, 8]
    column_values_code = df.iloc[:, 7]

    for len in range(column_values.size):
        if (column_values[len] == "項目"):
            if ({column_values[len+1]:column_values_code[len+1]} not in return_value):
                return_value.append({column_values[len+1]:column_values_code[len+1]})
    
    return return_value

def excel_type_read(df):
    type_value = []
    key_list = []
    return_value = {}
    list_data = ""

    column_values = df.iloc[:, 10]
    column_values_code = df.iloc[:, 9]
    column_values_list = df.iloc[:, 8]

    for len in range(column_values.size):
        if (column_values_list[len] == "項目"):
            if(list_data != column_values_list[len+1]):
                list_data = column_values_list[len+1]
                type_value.clear()
        if (column_values[len] == "種類"):
            if ({column_values[len+1].strip():str(column_values_code[len+1])} not in type_value):
                type_value.append({column_values[len+1].strip():str(column_values_code[len+1])})
                return_value.update({list_data:copy.deepcopy(type_value)})

    key_list = get_key_array(return_value)

    return key_list, return_value


def execl_size_read(df, key_list: list):
    size_value = []
    storage_list = []
    storage_list = []
    return_value = {}
    type_data = ""

    column_values = df.iloc[:, 12]
    column_values_code = df.iloc[:, 11]
    column_values_type = df.iloc[:, 10]

    for longth in range(column_values.size):
        if (column_values_type[longth] == "種類"):
            if(type_data != column_values_type[longth+1]):
                type_data = column_values_type[longth+1]

        if (column_values[longth] != "零件尺寸" and column_values[longth] != "種類" and pd.notna(column_values[longth])):
            storage_list.append([type_data,column_values[longth],longth])
    
    for item in key_list:
        size_value.clear()
        for i in range(len(storage_list)):
            if (storage_list[i][0] == item.strip()):
                if ({str(column_values[storage_list[i][2]]).strip():str(column_values_code[storage_list[i][2]])} not in size_value):
                    size_value.append({str(column_values[storage_list[i][2]]).strip():str(column_values_code[storage_list[i][2]])})
                    return_value.update({item:copy.deepcopy(size_value)})
        

    return return_value

def execl_percentage_read(df, key_list: list):
    percentage_value = []
    storage_list = []
    return_value = {}
    type_data = ""

    column_values = df.iloc[:, 14]
    column_values_code = df.iloc[:, 13]
    column_values_type = df.iloc[:, 10]

    for longth in range(column_values.size):
        if (column_values_type[longth] == "種類"):
            if(type_data != column_values_type[longth+1]):
                type_data = column_values_type[longth+1]

        if (column_values[longth] != "%數" and pd.notna(column_values[longth])):
            storage_list.append([type_data,column_values[longth],longth])

    for item in key_list:
        percentage_value.clear()
        for i in range(len(storage_list)):
            if (storage_list[i][0] == item):
                percentage_value.append({str(column_values[storage_list[i][2]]).strip().replace('\u3000','').replace(' ',''):str(column_values_code[storage_list[i][2]])})
                return_value.update({item:copy.deepcopy(percentage_value)})

    return return_value

def execl_capacity_read(df, key_list: list):
    capacity_value = []
    storage_list = []
    return_value = {}
    type_data = ""

    column_values = df.iloc[:, 16]
    column_values_code = df.iloc[:, 15]
    column_values_type = df.iloc[:, 10]

    for longth in range(column_values.size):
        if (column_values_type[longth] == "種類"):
            if(type_data != column_values_type[longth+1]):
                type_data = column_values_type[longth+1]

        if (column_values[longth] != "電容值" and column_values[longth] != "電阻值" and column_values[longth] != "PCB名稱" and column_values[longth] != "零件名稱" and pd.notna(column_values[longth])):
            storage_list.append([type_data,column_values[longth],longth])

    for item in key_list:
        capacity_value.clear()
        for i in range(len(storage_list)):
            if (storage_list[i][0] == item):
                capacity_value.append({str(column_values[storage_list[i][2]]).strip():str(column_values_code[storage_list[i][2]])})
                return_value.update({item:copy.deepcopy(capacity_value)})

    return return_value

def execl_voltage_read(df, key_list: list):
    voltage_value = []
    storage_list = []
    return_value = {}
    type_data = ""

    column_values = df.iloc[:, 18]
    column_values_code = df.iloc[:, 17]
    column_values_type = df.iloc[:, 10]

    for longth in range(column_values.size):
        if (column_values_type[longth] == "種類"):
            if(type_data != column_values_type[longth+1]):
                type_data = column_values_type[longth+1]

        if (column_values[longth] != "電壓" and pd.notna(column_values[longth])):
            storage_list.append([type_data,column_values[longth],longth])

    for item in key_list:
        voltage_value.clear()
        for i in range(len(storage_list)):
            if (storage_list[i][0] == item):
                voltage_value.append({str(column_values[storage_list[i][2]]).strip():str(column_values_code[storage_list[i][2]])})
                return_value.update({item:copy.deepcopy(voltage_value)})

    return return_value

def execl_manufacturer_read(df, key_list: list):
    manufacturer_value = []
    storage_list = []
    return_value = {}
    type_data = ""

    column_values = df.iloc[:, 20]
    column_values_code = df.iloc[:, 19]
    column_values_type = df.iloc[:, 10]

    for longth in range(column_values.size):
        if (column_values_type[longth] == "種類"):
            if(type_data != column_values_type[longth+1]):
                type_data = column_values_type[longth+1]

        if (column_values[longth] != "廠商" and pd.notna(column_values[longth])):
            storage_list.append([type_data,column_values[longth],longth])

    for item in key_list:
        manufacturer_value.clear()
        for i in range(len(storage_list)):
            if (storage_list[i][0] == item):
                manufacturer_value.append({str(column_values[storage_list[i][2]]).strip():str(column_values_code[storage_list[i][2]])})
                return_value.update({item:copy.deepcopy(manufacturer_value)})

    return return_value

def execl_supplier_read(df, key_list: list):
    manufacturer_value = []
    storage_list = []
    return_value = {}
    type_data = ""

    column_values = df.iloc[:, 22]
    column_values_code = df.iloc[:, 21]
    column_values_type = df.iloc[:, 10]

    for longth in range(column_values.size):
        if (column_values_type[longth] == "種類"):
            if(type_data != column_values_type[longth+1]):
                type_data = column_values_type[longth+1]

        if (column_values[longth] != "供應商" and pd.notna(column_values[longth])):
            storage_list.append([type_data,column_values[longth],longth])

    for item in key_list:
        manufacturer_value.clear()
        for i in range(len(storage_list)):
            if (storage_list[i][0] == item):
                manufacturer_value.append({str(column_values[storage_list[i][2]]).strip():str(column_values_code[storage_list[i][2]])})
                return_value.update({item:copy.deepcopy(manufacturer_value)})

    return return_value



# df = excel_file_read('曜璿東命名規則 20240605-2.xlsx', '命名規則')
# df2 = excel_file_read('曜璿東命名規則 20240605-2.xlsx', '電容種類規則')

# add_capacity(df2)

# print(excel_list_read(df))
# list_data, data = excel_type_read(df)
# print(list_data)
# print(execl_size_read(df, list_data))
# print(execl_percentage_read(df, list_data))
# print(execl_capacity_read(df, list_data))
# execl_voltage_read(df, list_data)
# execl_manufacturer_read(df, list_data)
# print(execl_supplier_read(df, list_data))