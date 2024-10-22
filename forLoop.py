### Part One -- your code goes here. 

#list of numbers from 1-10
#square it and keep going until last num in list done

numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

for number in numbers :
    square = number * number
    print( "the square of ", number , "*" , number , " is ", square )
    number = number + 1