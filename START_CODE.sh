#!/bin/bash

clear
echo "STARTING THE PROCESS...!"
echo "Enter the Name of the Project"
read project_name
echo ""
echo "PLEASE WAIT WHILE I CREATE THE REQUIRED FOLDERS AND FILES FOR YOU......"
echo ""
cd $HOME/Documents/
mkdir $project_name
echo "I have created a Project Folder for You !!"
echo "AT:$HOME/Documents/$project_name"     
cp create_project.py -f -t $HOME/Documents/$project_name                            #Change the pyhon file directory after copying the file to the bin or executlabe section of the linux
echo ""                                                    
cd $HOME/Documents/$project_name
touch temp.txt

python3 create_project.py $project_name $HOME/Documents/$project_name               #Using python file handling to create and name the Project
#process_exit_status = $?

if [ "$?" -ne 0 ]; 
then
    clear
    echo "SUCCESSFULLY CREATED THE PROJECT DIRECTORY AND FILE"
    echo "PRESS ANY KEY TO EXIT......."
    read 
else
    #clear
    echo "PROCESS FAILED"
    echo "PRESS ANY KEY TO CONTINUE....."                                                           #RECURSE HERE   
    read
fi
