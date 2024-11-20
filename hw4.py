import sys
import build_data
import county_demographics
import data
import os

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]


#TASK 1
#Main code below operations
#INPUTS: a single command-line argument (with an 'operations' file)
#OUTPUTS:
#PURPOSE

#OPERATIONS

#FIX DISPLAY FUNCTION
def display(data: dict) -> dict:
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
        if param2 not in attribute_top:
            return("ERROR WITH PARAMETER GIVEN")
        elif param2 in attribute_top:
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
        if param2 not in attribute_top:
            return("ERROR WITH PARAMETER GIVEN")
        elif param2 in attribute_top:
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
        if param2 not in attribute_top:
            return("ERROR WITH PARAMETER GIVEN")
        if param2 in attribute_top:
            pop_portion+= county.population['2014 Population']*(attribute_top[param2])/100
    print("2014 {} population: {}".format(field, pop_portion))

    return pop_portion

def percent_field(data, field) -> (float):
    tot = population_total(data)
    if tot == 0:
        print("the given data set is blank.")
        return("the given data set is blank")
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
    print("Number of initial entries: {}".format(len(data)))

    for line in lines:
        liney = line.strip("\n")
        line_list = liney.split(":")

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
                population_field(data, line_list[1])
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
    return "-"

if __name__ == '__main__':

    print(opening_data_and_file(sys.argv[1], reduced_data))


#TASK 2:
#Operations files: task2 a, b, c, and d









