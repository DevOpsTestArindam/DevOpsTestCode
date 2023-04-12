lines_1 = ['Text', 'this is the example to show how the user can write in the text file by using Python']  
with open ('text.txt', 'w') as file:  
    for line_1 in lines_1:  
        file.write(line_1)  
        file.write('\n')  