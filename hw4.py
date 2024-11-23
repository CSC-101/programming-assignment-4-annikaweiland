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
#input: A list of data type CountyDemographics
#output: A string of all counties in the given data list
#purpose: To display the counties in data in a user-friendly manner
def display(data: list[data.CountyDemographics]) -> str:
    for county in data:
        print ("COUNTY, ST: {}, {} \n \t AGES: {} \n \t EDUCATION: {} \n \t ETHNICITIES: {} \n \t EDUCATION: {}".format(county.county, county.state, county.age, county.education, county.ethnicities, county.income))
    if data == []:
        print("There are no counties in this dataset.")
    exit(1)

#input: A list containing CountyDemographics, and a given str that is the input state.
#output: A str stating the amount of entries
#purpose: To find out how many of the county demographics have the input state as their state
def filter_state(data: list[data.CountyDemographics], input_st: str) -> list:
    filtered_list = [county for county in data if county.state == input_st]
    data = filtered_list
    amt_entries = len(data)
    print ("Filter: state == {} ({} entries)".format(input_st, amt_entries))
    return data

#input: A list containing CountyDemographics, a field that is a str, and a float number.
#output: A list of CountyDemographics that fit the given parameters.
#purpose: To filter the data list by the given field percentages that are greater than the given percentage value.
def filter_gt(data: list[data.CountyDemographics], field: str, num = float) -> list:
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

#input: A list containing CountyDemographics, a field that is a str, and a float number.
#output:  A list of CountyDemographics that fit the given parameters.
#purpose: To filter the data list by the given field percentages that are greater than the given percentage value.
def filter_lt(data: list[data.CountyDemographics], field: str, num: float) -> list:
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

#input: A list containing CountyDemographics
#output: An integer value representative of the total population of the list of counties.
#purpose: To determine the total population of the given data set.
def population_total(data: list[data.CountyDemographics]) -> int:
    total_pop = 0
    for county in data:
        total_pop += county.population['2014 Population']
    return total_pop

#input: A list containing CountyDemographics, and a given field that is a str.
#output: A float value representative of a population.
#purpose: To return the total population in a given field in a given list of counties.
def population_field(data: list[data.CountyDemographics], field: str) -> float:
    pop_portion = 0
    field_list = field.split(".")
    param1 = field_list[0].lower()
    param2 = field_list[1]
    for county in data:
        attribute_top = getattr(county, param1, None)
        pop_portion+= county.population['2014 Population']*(attribute_top[param2])/100
    return pop_portion

#input: A list of data type CountyDemographics and a field that is a str.
#output: A float value that is representative of the percentage in the given population of a given field.
#purpose: To determine the percent of a given field in the given population of counties in the data.
def percent_field(data: list[data.CountyDemographics], field: str) -> float:
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
#input: A str that is the name of a file (or a command-line argument containing a str that is the name of a file), and a list of data type CountyDemographics
#output: A string value.
#purpose: To open and read the given op file, and perform the given functions in op file on the parameter data
def opening_data_and_file(op_file: str, data = list[data.CountyDemographics]) -> str:
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
#change file in command line to test out different files
    print(opening_data_and_file(sys.argv[1], build_data.get_data()))

#Operations files: task2 a, b, c, and d









