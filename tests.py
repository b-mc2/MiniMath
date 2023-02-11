from minimath import MiniMath

minimath = MiniMath()


A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]


assert minimath.matrix_add(A, B) == [[6, 8], [10, 12]]
assert minimath.matrix_subtract(A, B) == [[-4, -4], [-4, -4]]
assert minimath.scalar_multiply(A, 3) == [9, 21]
assert minimath.scalar_multiply(A, B) == [[19, 22], [43, 50]]
assert minimath.dot(A[0], B[0]) == 17
assert minimath.cosine_similarity(A[0], B[0]) == 0.9734171683335761
assert minimath.matrix_product(A, B) == [[19, 22], [43, 50]]
assert minimath.smallest_pair(A) == [1, 2]
assert minimath.largest_pair(A) == [3, 4]
assert minimath.max_index_values(A, B) == [[5, 6], [7, 8]]
assert minimath.cross_sum(A[1], B[1]) == [10, 12]
assert minimath.check_prime(17) == True
assert minimath.find_mersenne_prime(15) == [1, 3, 7, 31, 127, 8191]
assert minimath.factoral(10) == 3628800