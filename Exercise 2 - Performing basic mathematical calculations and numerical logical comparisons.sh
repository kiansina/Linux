"""
Exercise 2 - Performing basic mathematical calculations and numerical logical
comparisons
"""

"""
In this exercise, you will create a Bash script that performs basic arithmetic
calculations on two integers entered by the user. You will also use logical
comparisons to determine which calculation leads to the greatest result.
"""

"""
2.1. Create a Bash script
"""

echo '#!/bin/bash' > exercise2.sh


chmod u+x exercise2.sh
nano exercise2.sh

#add followings:
echo 'please enter your first integer'
read int1
echo 'please enter your second integer'
read int2

echo "The sum of the integers is $(($int1+$int2))"
echo "The product of your integers $int1 and $int2 is $(($int1*$int2))"

#now you can run
./exercise2.sh



"""
2.2. Add logic to your script
"""

"""
Add logic to your script that determines whether the sum is greater than, less
than, or equal to the product. Display an appropriate statement corresponding to
each possible result.
"""

nano exercise.sh

#add the following:

sum=$(($int1+$int2))
product=$(($int1*$int2))

if [[ $sum < $product ]]
then
  echo "the sum=$sum is less than the product=$product"
elif [[ $sum == $product ]]
then
  echo -e "the sum and product are equal so the integeres are 2 and sum \nas well as product is equal ti $sum"
else
  echo "the sum=$sum is more than the product=$product"
fi

# Now you can run it
./exercise2.sh
