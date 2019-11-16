# weight = int(input('Enter your weight: '))
# years = int(input('How old do you want to calculate your weight: '))
#
#
# def moon_weight():
#     for year in range(1, years):
#         weight = weight + 1
#         moon_weight = weight * 0.165
#         print('Year %s is %s' % (year, moon_weight))


weight = 80
for year in range(1, 16):
    weight = weight + 1
    moon_weight = weight * 0.165
    print('Year %s is %s' % (year, moon_weight))