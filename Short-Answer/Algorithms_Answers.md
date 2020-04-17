#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear time O(n) because the function grows as the input increases n times


b) Cuadratic time O(n^2) because its performance is directly proportional to the square of the size of the input data set.  


c) Linear time O(n)  because its performance will grow linearly and in direct proportion to the size of the input data set.

## Exercise II

- Need to find the lethal floor where the egg will break 
- Anything equal to or higher will break the egg if thrown down
- We can now split the amount of floors in half
- Throw the egg to check if breaks
- If it breaks we know that lethal floor (f) is in the lower half 
    - We then repeat the step to split the floor amount in half again and continue
- If the egg does not break we Know the lethal floor (f) has to be higher
    - Repeat the step to split the floor amount in half and continue

I think since I will probably have to loop and reduce the input in half every time I think the time complexity will be faster, I think it is O(log n) thus having a logaritmic time complexity.

