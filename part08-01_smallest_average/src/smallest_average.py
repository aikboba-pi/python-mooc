# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    person1AvgRes = (person1['result1'] + person1['result2'] + person1['result3']) / 3
    person2AvgRes = (person2['result1'] + person2['result2'] + person2['result3']) / 3
    person3AvgRes = (person3['result1'] + person3['result2'] + person3['result3']) / 3

    personsMap = { person1AvgRes: person1, person2AvgRes: person2, person3AvgRes: person3 }

    return personsMap[min(person1AvgRes, person2AvgRes, person3AvgRes)]