# MiniMath
### A small math library with no imports and only one-liner functions

Welcome to MiniMath, the dependency free one-liner wonder! 

This is designed with tiny functions that fit in a single line! Each and every function in this Class exists on a single line, but don't be fooled, just because 
it's on a single line doesn't mean it's easy to understand. In fact, it's quite the opposite. I've tried to pack a lot of functionality into a tiny space, so you may need to take a closer look to fully grasp what's going on. 

I've included functions to calculate mean, median, mode, perform 
matrix operations, calculate standard deviations, variance, dot products, cosine similarity, calculate MSE, percentiles,
check if numbers are prime, multiply scalars, calculate factorials, and even remove outliers from lists. Each with just 
a single line of code! But beware, this Class is not to be taken seriously. It's a playful experiment that heavily 
utilizes map, lambda, filter, zip, and other features of Python to write functions in the tiniest way possible. Don't 
use this for any mission-critical calculations.

So go ahead, have fun with MiniMath. You can impress your friends with your single-liner skills and make them shake 
their head at the ridiculousness of it at the same time.

#### Current Functions supported
- Mean, Median, Mode
- Square Root
- Least Common Item 
  - Returns the item of an iterable that occurs the fewest amount of times 
- Matrix Addition, Subtraction, Product
- Scalar Multiplication
- Dot Products
  - Similar to `np.dot()`
- Exponentials
  - Similar to `np.exp()`
- Sigmoid
- Cosine Similarity
- Jaccard and Hamming Distances (for iterables including strings)
- Pythagorean distances (2D and n-D)
- Mean Squared Error
- Least Squares Regression
  - Returns LSR line when given two iterables
  - ToDo: Return function, add predict ability
- Reshape
  - Reshapes a list into N lists of lists
- Smallest and Largest Pairs
  - Returns the pair with smallest or largest difference between iterables
- Max Index Values
  - Checks values between two iterables at each index and returns the higher value
- Percentile
- Variance, Variance Sample
- Standard Deviation, Standard Deviation Sample
- Cross Sum
  - Takes two iterables and sums the values by each index
- Sort Dictionary by Values
- Sort List of Dictionaries by values
- Filter List Min/Max
  - Filters a list down by values above min, or below max
- Zip/Unzip Lists
  - Zips or Unzips two lists and returns lists of lists
- Combine Lists String
  - Combines two lists with a custom string separator
- Check Prime
  - Checks if a number is prime or not, returns boolean
- Find Primes/Find Mersenne Primes
  - Finds all prime numbers up to N, or finds only Mersenne Primes up untill N (being the exponent)
- ROT13 cipher, XOR Cipher
- Nested Tuple It/List It
  - Convert nested tuples to lists, or lists to tuples
- Factoral
- Check N Divisible by X,Y
  - Takes in N, X, and Y and returns Boolean checking if N is divisible by X and Y
- Find odd/even below N
  - Returns a list of odd or even numbers below the value N
- Remove Outliers
  - Takes an iterable and N (number of standard deviations from mean) and returns values that fall within N


**Some examples:**

#### Mean Squared Error
```python
A, B = [41, 45, 49, 47, 44], [43.6, 44.4, 45.2, 46, 46.8]

mse = lambda A, B: sum(map(lambda x: (x[0] - x[1]) ** 2, zip(A, B))) / len(A)

mse(A,B)
# 6.079999999999994
```

#### Standard Deviation
```python
A = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]

std = lambda A: (sum(map(lambda x: (x - sum(A) / len(A)) ** 2, A)) / len(A)) ** 0.5

std(A)
# 3.6193922141707713
```

#### Cosine Similarity
```python
A, B = [3, 2, 0, 5], [1, 0, 0, 0]


# Flat format
cosine_similarity = (lambda A, B: sum(x * y for x, y in zip(A, B)) / (sum([i**2 for i in A])**(1/2) * sum([i**2 for i in B])**(1/2)))


# In Black Format
cosine_similarity = lambda A, B: sum(x * y for x, y in zip(A, B)) / (
    sum([i**2 for i in A]) ** (1 / 2) * sum([i**2 for i in B]) ** (1 / 2)
)

cosine_similarity(A, B)
# 0.48666426339228763
```

#### Remove Outliers (N Standard Deviations from Mean)
```python
A = [10, 8, 10, 8, 2, 7, 9, 3, 34, 9, 5, 9, 25]
# Mean is 10.692307692307692


# Flat format
remove_outliers = lambda A, n: list(filter(lambda x: (sum(A)/len(A) - n * (sum(map(lambda x: (x-sum(A)/len(A))**2, A))/len(A))**0.5) <= x <= (sum(A)/len(A) + n * (sum(map(lambda x: (x-sum(A)/len(A))**2, A))/len(A))**0.5), A))


# In Black Format
remove_outliers = lambda A, n: list(
    filter(
        lambda x: (
            sum(A) / len(A)
            - n * (sum(map(lambda x: (x - sum(A) / len(A)) ** 2, A)) / len(A)) ** 0.5
        )
        <= x
        <= (
            sum(A) / len(A)
            + n * (sum(map(lambda x: (x - sum(A) / len(A)) ** 2, A)) / len(A)) ** 0.5
        ),
        A,
    )
)

remove_outliers(A, 2)
# [10, 8, 10, 8, 2, 7, 9, 3, 9, 5, 9, 25]
remove_outliers(A, 1)
# [10, 8, 10, 8, 7, 9, 3, 9, 5, 9]
remove_outliers(A, 0.25)
# [10, 10, 9, 9, 9]
```

#### Matrix Subtraction
```python
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[9,8,7],
     [6,5,4],
     [3,2,1]]


matrix_subtract = lambda A, B: list(map(lambda x, y: [a - b for a, b in zip(x, y)], A, B))

matrix_subtract(A, B)
# [[-8, -6, -4],
#  [-2,  0,  2], 
#  [ 4,  6,  8]]
```

#### Matrix Product
```python
A = [[1, 2], 
     [3, 4]]

B = [[5, 6],
     [7, 8]]


matrix_product = lambda A, B: [[sum(ea * eb for ea, eb in zip(a, b)) for b in zip(*B)] for a in A]

matrix_product(A,B)
# [[19, 22],
#  [43, 50]]
```

#### Dot Product
```python
A, B = [2,7,1], [8,2,8]


dot = lambda A, B: sum(x * y for x, y in zip(A, B))

dot(A, B)
# 38
```

---
### Q&A
**Q:** **Why would someone write this?**

**A:** MiniMath was written as a playful experiment to see if it was possible to write functions that fit in a single line.
It's a demonstration of the power of Python's functional programming features and a showcase of the art of coding creatively.

**Q:** **Is MiniMath suitable for production use?**

**A:** No, MiniMath is not suitable for production use. It's a fun experiment, but not meant to be used in any serious calculations.
The code is intentionally compact, which can make it hard to understand, debug, and maintain. There are also many instances where these 
functions don't handle a wide range of input types, like you'd see in Numpy or other libraries. On the plus side with very little 
changes you can copy and paste a particular function into your program and use it if you just want one function.

**Q:** **Is MiniMath an efficient way to perform calculations?**

**A:** Efficiency was not a primary concern when designing MiniMath. The focus was on writing functions that fit in a single line. 
As a result, the code may not be optimized for performance, but considering it's regular python, some functions may be faster 
than importing a larger library to perform one calculation.

That being said testing `MiniMath.dot()` vs `np.dot()` on two lists of 10M integers ranging from 1-10,000 yields these results. 
Just remember that Numpy's dot is much more robust on input data.
```python
timeit.timeit("minimath.dot(A,B)", number=100, globals=globals())
55.66622825601371
timeit.timeit("np.dot(A,B)", number=100, globals=globals())
129.96896048099734
```

**Q:** **Can I contribute to MiniMath or make corrections?**

**A:** Yes! That would be great, MiniMath has been a learning experience in both better understanding Python standard features 
and better understanding the underlying formulas themselves, there's bound to be tweaks or errors to correct. If you want 
to submit a new function, just make sure the function fits on a single line and doesn't require any imports, even to Python 
Math, or other standard libraries.

**Q:** **I tried to copy and paste a single line but it didn't work**

**A:** This is something that's still being considered, MiniMath is about making _functions_ that fit on a single line, but 
as the MiniMath object, there's references to other one-line functions, like `self.mean()` which seems to defeat the purpose 
of one-line functions. The library would probably be _truer_ to not do this, to incorporate the logic right on the same line, but
I'm still debating doing that. For now any function that references another could simply plug in that function's logic. `lambda self` is 
also something that was added to make these functions work within the `MiniMath` object, though aren't needed if you're just copying and pasting
a single line.
