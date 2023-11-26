d = {}
with open("Dictionary.txt", encoding="utf-8") as file:
    for line in file:
        line = line.split(":") #разделение на списки по :
        subject = line[0]
        activities = line[1].split()
        total_hours = 0
        for activity in activities:
            hours = int(activity.split('(')[0])
            total_hours += hours
            d[subject] = total_hours
print(d)