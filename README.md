# MiniMath
### A small math library with no imports and only one-liner functions

Welcome to MiniMath, the dependency free one-liner wonder! 

This is designed with tiny functions that fit in a single line! Each and every function in this Class exists on a single line, but don't be fooled, just because 
it's on a single line doesn't mean it's easy to understand. In fact, it's quite the opposite. We've packed a lot of functionality into a tiny space, so you may need to 
take a closer look to fully grasp what's going on. 

We've included functions to calculate mean, median, mode, perform 
matrix operations, calculate standard deviations, variance, dot products, cosine similarity, calculate MSE, percentiles,
check if numbers are prime, multiply scalars, calculate factorials, and even remove outliers from lists. Each with just 
a single line of code! But beware, this Class is not to be taken seriously. It's a playful experiment that heavily 
utilizes map, lambda, filter, zip, and other features of Python to write functions in the tiniest way possible. Don't 
use this for any mission-critical calculations.

So go ahead, have fun with MiniMath. You can impress your friends with your single-liner skills and make them shake 
their head at the ridiculousness of it at the same time.

---
### Q&A
**Q:** **Why would someone write this?**

**A:** MiniMath was written as a playful experiment to see if it was possible to write functions that fit in a single line.
It's a demonstration of the power of Python's functional programming features and a showcase of the art of coding creatively.

**Q:** **Is MiniMath suitable for production use?**

**A:** No, MiniMath is not suitable for production use. It's a fun experiment, but not meant to be used in any serious calculations.
The code is intentionally compact, which can make it hard to understand, debug, and maintain. On the plus side with very little 
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

**Q:** **Why are there different versions of MiniMath .py files?**

**A:** This is something that's still being considered, MiniMath is about making functions that fit on a single line, but 
as the MiniMath object, there's references to other one-line functions, like `self.mean()` which seems to defeat the purpose 
of one-line functions. The library would probably be _truer_ to not do this, to incorporate the logic right on the same line.
