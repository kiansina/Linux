"""
In this exercise, you will create a report based on a supplied dataset using the
CSV format. You will extract the columns of the dataset into separate arrays and
create a new column using arithmetic and array logic. Finally, you will combine
the dataset with the new column and save the resulting report as a CSV file.
"""

"""
3.1. Download a CSV file to your current working directory
"""

"""
The file, arrays_table.csv, is located at the following url:
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv
"""

csv_file="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv"
wget $csv_file


"""
3.2. Display the CSV file to understand what it looks like
"""
cat arrays_table.csv

"""
3.3. Create a Bash script that parses table columns into 3 arrays
"""
echo '#!/bin/bash'>exercise3.sh
nano exercise3.sh

#add following in nano:

csv_file="./arrays_table.csv"
# parse table columns into 3 arrays
column_0=($(cut -d "," -f 1 $csv_file))
column_1=($(cut -d "," -f 2 $csv_file))
column_2=($(cut -d "," -f 3 $csv_file))
# print first array
echo "Displaying the first column:"
echo "${column_0[@]}"


#close nano

chmod u+x exercise3.sh
./exercise3.sh




"""
3.4. Create a new array as the difference of the third and second columns.
"""

# add this in script:


## Create a new array as the difference of columns 1 and 2
# initialize array with header
column_3=("column_3")
# get the number of lines in each column
nlines=$(cat $csv_file | wc -l)
echo "There are $nlines lines in the file"
# populate the array
for ((i=1; i<$nlines; i++)); do
  column_3[$i]=$((column_2[$i] - column_1[$i]))
done
echo "${column_3[@]}"




"""
3.5. Create a report by combining your new column with the source table
"""

## Combine the new array with the csv file
# first write the new array to file
# initialize the file with a header
echo "${column_3[0]}" > column_3.txt
for ((i=1; i<nlines; i++)); do
  echo "${column_3[$i]}" >> column_3.txt
done
paste -d "," $csv_file column_3.txt > report.csv
