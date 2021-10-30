import os

print("Please copy the folder destination where you would like to operate the files rename: ",end ='')
folder = input()
print("Please select the name which will be iterated: ", end = '')
name = input()
print("Please select the extension of the renamed files: ",end = '')
extension = input()

count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + "\\" + file_name

    # Adding the count to the new file name and extension
    destination = folder + "\\" + name + "_" + str(count) + "." + extension

    # Renaming the file
    os.rename(source, destination)
    count += 1
print('All Files Renamed')

print('New Names are')
# verify the result
res = os.listdir(folder)
print(res)
