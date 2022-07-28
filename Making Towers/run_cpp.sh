#!/bin/bash
g++ main.cpp -o main
# if no error continue
if [ $? -eq 0 ]; then
    ./main < test.txt
else
    echo "----------Compilation error----------"
fi
