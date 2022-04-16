#!/bin/python3
if __name__ == '__main__':
    athletes_and_attributes = input().split(" ")
    number_of_athletes = athletes_and_attributes[0]
    number_of_attributes = athletes_and_attributes[1]
    athletes_attributes = []
    for current_athlete in range(int(number_of_athletes)):
        athlete_attributes = input().split(" ")[:int(number_of_attributes)]
        athlete_attributes = [int(attribute) for attribute in athlete_attributes]
        athletes_attributes.append(athlete_attributes)
    index_sort = input()
    index_sort = int(index_sort)
    athletes_attributes.sort(key=lambda x: x[index_sort])
    for athlete_attributes in athletes_attributes:
        print(" ".join(str(attribute) for attribute in athlete_attributes))
