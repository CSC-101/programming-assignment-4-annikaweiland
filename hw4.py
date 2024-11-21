import sys
import build_data
import county_demographics
import data
import os

#TASK 1
#Main code below operations
#INPUTS: a single command-line argument (with an 'operations' file)
#OUTPUTS:
#PURPOSE

#OPERATIONS

def display(data: dict) -> str:
    for county in data:
        print ("COUNTY, ST: {}, {} \n \t AGES: {} \n \t EDUCATION: {} \n \t ETHNICITIES: {} \n \t EDUCATION: {}".format(county.county, county.state, county.age, county.education, county.ethnicities, county.income))
    if data == []:
        print("There are no counties in this dataset.")
    exit(1)

def filter_state(data, input_st: str) -> list:
    filtered_list = [county for county in data if county.state == input_st]
    data = filtered_list
    amt_entries = len(data)
    print ("Filter: state == {} ({} entries)".format(input_st, amt_entries))
    return data

def filter_gt(data, field: str, num = float) -> list:
    field_list = field.split(".")
    param1 = field_list[0].lower()
    param2 = field_list[1]
    filter_gt_list = []
    for county in data:
        attribute_top = getattr(county, param1, None)
        if attribute_top[param2] > num:
            filter_gt_list.append(county)
    entries = len(filter_gt_list)
    data = filter_gt_list
    print("Filter: {} gt {}% ({} entries)".format(field, num, entries))
    return data

def filter_lt(data, field: str, num: float) -> list:
    field_list = field.split(".")
    param1 = field_list[0].lower()
    param2 = field_list[1]
    filter_lt_list = []
    for county in data:
        attribute_top = getattr(county, param1, None)
        if attribute_top[param2] < num:
            filter_lt_list.append(county)
    entries = len(filter_lt_list)
    data = filter_lt_list
    print("Filter: {} lt {}% ({} entries)".format(field, num, entries))
    return data

def population_total(data: list[dict]) -> int:
    total_pop = 0
    for county in data:
        total_pop += county.population['2014 Population']
    return total_pop

def population_field(data, field: str) -> float:
    pop_portion = 0
    field_list = field.split(".")
    param1 = field_list[0].lower()
    param2 = field_list[1]
    for county in data:
        attribute_top = getattr(county, param1, None)
        pop_portion+= county.population['2014 Population']*(attribute_top[param2])/100
    return pop_portion

def percent_field(data, field) -> float:
    tot = population_total(data)
    if tot == 0:
        print("the given data set is blank.")
        return 0
    try:
        tot_portion = population_field(data, field)
        percentage = (tot_portion/tot)*100
        print("2014 {} percentage: {}".format(field, percentage))
    except:
        print("ERROR OCCURRED")
    return percentage


#Main code:
def opening_data_and_file(op_file: str, data = list[dict]): #output is the FILE BEING OPENED
#input would be from command line - sys.argv[1] - op_file
#data is build_data.get_data() at first, but updates depending on the operation
    try:
        file = "inputs/"+op_file
        with open(file) as file:
            lines = file.readlines()

    except FileNotFoundError as e:
        return e

    print(op_file)
    print("Number of initial entries: {}".format(len(data)))

    for line in lines:
        line1 = line.strip("\n")
        liney = line.strip()
        line_list = liney.split(":")

        if not liney:
            continue

        try:
            if len(line_list) == 3:
                num = float(line_list[2])

        except ValueError as e:
            num = "ERROR"
            print("VALUEERROR ON LINE <{}>".format(line))
            continue

        if len(line_list)>=4:
            print("ERROR ON LINE <{}>".format(line))
            continue

        if line_list[0] == "population-total":
            try:
                pop = population_total(data)
                print("2014 population: {}".format(pop))
            except:
                print("ERROR ON LINE <{}>".format(line))
                continue

        elif line_list[0] == "population":
            try:
                pop = population_field(data, line_list[1])
                print("2014 {} population: {}".format(line_list[1], pop))

            except:
                print("ERROR ON LINE <{}>".format(line))
                continue

        elif line_list[0] == "percent":
            try:
                percent_field(data, line_list[1])
            except:
                print("ERROR ON LINE <{}>".format(line))
                continue

        elif line_list[0] == "filter-lt":
            try:
                pot_data = filter_lt(data, line_list[1], num)
                if type(pot_data) == str:
                    data = data
                else:
                    data = pot_data
            except:
                print("ERROR ON LINE <{}>".format(line))
                continue

        elif line_list[0] == "filter-gt":
            try:
                pot_data = filter_gt(data, line_list[1], num)
                if type(pot_data) == str:
                    data = data
                else:
                    data = pot_data
            except:
                print("ERROR ON LINE <{}>".format(line))
                continue

        elif line_list[0] == "filter-state":
            try:
                pot_data = filter_state(data, line_list[1])
                if type(pot_data) == str:
                    data = data
                else:
                    data = pot_data
            except:
                print("ERROR ON LINE <{}>".format(line))
                continue

        elif line_list[0] == "display":
            print(display(data))
        else:
            print("ERROR ON LINE <{}>".format(line))
    return "all file lines processed\n"


#EXECUTION OF ALL FILES:

if __name__ == '__main__':
# pop.ops: name in command line
    print(opening_data_and_file(sys.argv[1], build_data.get_data()))
#pop_field.ops
    print(opening_data_and_file("pop_field.ops", build_data.get_data()))
#percent_fields.ops
    print(opening_data_and_file("percent_fields.ops", build_data.get_data()))
#high_school_lt_60.ops
    print(opening_data_and_file("high_school_lt_60.ops", build_data.get_data()))
#filter_state.ops
    print(opening_data_and_file("filter_state.ops", build_data.get_data()))
#ca.ops
    print(opening_data_and_file("ca.ops", build_data.get_data()))
#bachelors_gt_60.ops
    print(opening_data_and_file("bachelors_gt_60.ops", build_data.get_data()))
#some_errors.ops
    print(opening_data_and_file("some_errors.ops", build_data.get_data()))
#TASK 2:
#Operations files: task2 a, b, c, and d









