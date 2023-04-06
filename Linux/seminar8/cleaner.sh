#! /bin/bash

directory=$1
if [ -z "${directory}" ]; 
        then
                echo "Use: $0 <a directory path>"
                exit 1
        else
                if [ -d "$directory" ]; 
                        then
                                for file in $(ls $directory | grep -E "\.(bak|tmp|backup)$"); 
                                        do
                                                filepath=$directory/$file
                                                rm -f $filepath
                                        done
                                echo "Cleaned!"
                        else
                                echo "There's no $directory directory"
                                exit 1
                fi
fi

