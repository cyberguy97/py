# try:
#     x = int(input('Type an integer here: '))
#     print(x)
# except:
#     print('GBAM!')
# else:
#     print('code success!')

with open('countries.txt', 'r') as coun_file:
    print(coun_file.readable())
    content = coun_file.read()
    print(content)
# File closes automatically here!

with open('countries.txt', 'r') as coun_file:
    print(coun_file.readlines())
    content = coun_file.read()
    print(content)
# File closes automatically here!
