
import os
import sys

project_name = sys.argv[1]
path_of_project_folder = sys.argv[2]
choice = 0
file_type = ""
x = True

print("Very Well !!\n1. C\n2. CPP\n3. JAVA\n4. PYTHON")
while(x):
        choice = int(input("\nNOW What Type Of The File You Want To Start With(INPUT NUM): "))
        if choice == 1:
            file_type = ".c"
            x=False
        elif choice == 2:
            file_type = ".cpp"
            x=False
        elif choice == 3:
            file_type = ".java"
            x=False
        elif choice == 4:
            file_type = ".py"
            x=False
        else:
            print("I BELIEVE WRONG CHOICES HAVE A REASON TO BE.....!\nSO, DOU YOU WANT TO QUIT THE IDEA FOR THE PROJECT !!(YES/NO)")
            temp = input()
            if temp == "NO" or temp == "N" or temp == "no" or temp == "n" :
                pass
            else:
                sys.exit(0)    

os.chdir(path_of_project_folder)
file_name = project_name + file_type
#print(file_type)
print("The "+file_name+" is Created")
os.rename("temp.txt",file_name)
file_object = open(file_name,"w+")
file_object.write("WELCOME TO THE "+project_name+" Project\nYou are all set to begin with right away!!\nBEST LUCK")
file_object.close()

sys.exit(1)
