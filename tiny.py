import os
directory = r'C:\Users\Nikolas\NPRCube'
filenames = []
for filename in os.listdir(directory + "\\data"):
    filenames.append(filename)
print(filenames)