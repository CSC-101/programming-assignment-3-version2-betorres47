# - programming assignment #3
# - cs 101 Professor Rathi
# - beto torres 2/27/2025

import county_demographics
from data import CountyDemographics


# - Task 1

#define population_total with country list of CountryDemographics as input and an int as output
def population_total(country: list[CountyDemographics]) -> int:
    total = 0                                       # create total
    for x in country:                               # for loop to sum population
        total += x.population["2024 Population"]    # sum population
    return total


# - Task 2

#define filter_by_state with objects list and state as input and a list of country demographics as output
def filter_by_state(l: list[CountyDemographics], state: str) -> list[CountyDemographics]:  # I need to get a list of county demographics and a state, then return a list of that county demographics of that state
    outlist = []                                    # create output list
    for x in l:                                     # for loop to change compare states
        if x.state == state:                        # compare states
            outlist.append(x)                       # append to the output list
    return outlist

# - Task 3

#define functions with inputs and outputs

def population_by_education(l: list[CountyDemographics], word: str) -> float:
    number = 0.0
    for x in l:                                                             # multiply the percentage that are educated by population total
       number += x.population["2014 Population"]*(x.education[word]/100)
    return number


def population_by_ethnicity(l:list[CountyDemographics], word:str) -> float:
    number = 0.0
    for x in l:
        number += x.population["2014 Population"] * (x.ethnicities[word]/100) # multiply the percentage that are educated by population total
    return number


def population_below_poverty_level(l:list[CountyDemographics]) -> float:
    number = 0.0
    for x in l:                                                               # multiply the percentage that are educated by population total
        number += x.population["2014 Population"] * (x.income["Persons Below Poverty Level"]/100)
    return number

# - Task 4

# for each function define the list and the string input and output
# find the population of people with the specified string and compare to total, make percentage

def percent_by_education(l:list[CountyDemographics], word:str) -> float:
    education = population_by_education(l, word)
    population = population_total(l)
    return (education/population)*100


def percent_by_ethnicity(l:list[CountyDemographics], word:str) -> float:
    ethnicity = population_by_ethnicity(l, word)
    population = population_total(l)
    return (ethnicity/population)*100

def percent_below_poverty_level(l:list[CountyDemographics]) -> float:
    belowPovertyLine = population_below_poverty_level(l)
    population = population_total(l)
    return (belowPovertyLine/population)*100

# - Task 5

# we take the list, word, percent as inputs and a list as outputs
# we then compare the percentage to the population percentage and append the list if the operation is true
# this list is returned as our output, some of the functions vary however they all follow the same principle of checking the percentage

def education_greater_than(l:list[CountyDemographics], word:str, percent:float) -> list[CountyDemographics]:
    outlist = []
    for x in l:
        if percent_by_education([x], word) > percent:
            outlist.append(x)
    return outlist


def education_less_than(l:list[CountyDemographics], word:str, percent:float) -> list[CountyDemographics]:
    outlist = []
    for x in l:
        if percent_by_education([x], word) < percent:
            outlist.append(x)
    return outlist


def ethnicity_greater_than(l:list[CountyDemographics], word:str, percent:float) -> list[CountyDemographics]:
    outlist = []
    for x in l:
        if percent_by_ethnicity([x], word) > percent:
            outlist.append(x)
    return outlist


def ethnicity_less_than(l:list[CountyDemographics], word:str, percent:float) -> list[CountyDemographics]:
    outlist = []
    for x in l:
        if percent_by_ethnicity([x], word) < percent:
            outlist.append(x)
    return outlist

def below_poverty_level_greater_than(l:list[CountyDemographics], percent:float) -> list[CountyDemographics]:
    outlist = []
    for x in l:
        if percent_below_poverty_level([x]) > percent:
            outlist.append(x)
    return outlist


def below_poverty_level_less_than(l:list[CountyDemographics], percent:float) -> list[CountyDemographics]:
    outlist = []
    for x in l:
        if percent_below_poverty_level([x]) < percent:
            outlist.append(x)
    return outlist

