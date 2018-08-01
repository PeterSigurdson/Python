directory_name = 'L:\workbooks\python'
team_file_name = 'Challenge1_output.txt'

f = open(directory_name+team_file_name,'w') 
f.write("HELLO!")
f.write(" **-- team members' names")
print(" type STOP to end entry of team members' names")

DATA_ENTRY = 'GO'

while (DATA_ENTRY == 'GO'):
    teammembername = input("State Team Member's Name and Student number in the form Name-StudentNumber:    ")  
    f.write("\n" + teammembername + "\n")
    print(' you entered ', teammembername )

    if (teammembername == "STOP"):
        DATA_ENTRY = 'STOP'
        print('data entry complete. you may view your file at ', directory_name, ' ', team_file_name)
        
        
f.close()
