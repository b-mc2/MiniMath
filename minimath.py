class MiniMath:
	mean = lambda self, A: sum(A) / len(A)
	median = lambda self, A: sorted(A)[int(len(A) / 2)]
	mode = lambda self, A: max(A, key=A.count)
	sqrt = lambda self, A: sum(A) ** 0.5 if hasattr(A, "__iter__") else A ** 0.5
	least_common_item = lambda self, A: min(A, key=A.count)
	matrix_add = lambda self, A, B: list(map(lambda x, y: [a + b for a, b in zip(x, y)], A, B))
	matrix_subtract = lambda self, A, B: list(map(lambda x, y: [a - b for a, b in zip(x, y)], A, B))
	scalar_multiply = (lambda self, A, B: [[sum(ea * eb for ea, eb in zip(a, b)) for b in zip(*B)] for a in A] if isinstance(B, list) else [sum(ea * B for ea in a) for a in A])
	matrix_product = lambda self, A, B: [[sum(ea * eb for ea, eb in zip(a, b)) for b in zip(*B)] for a in A]
	dot = lambda self, A, B: sum(x * y for x, y in zip(A, B))
	exp = lambda self, A: [2.718281**a for a in A] if hasattr(A, '__iter__') else 2.718281**A
	sigmoid = lambda self, A: 1.0/(1 + 2.718281**-A)
	cosine_similarity = (lambda self, A, B: self.dot(A, B) / (sum([i ** 2 for i in A]) ** (1 / 2) * sum([i ** 2 for i in B]) ** (1 / 2)))
	jaccard = lambda self, A, B: len(set(A).intersection(set(B))) / len(set(A).union(set(B)))
	hamming = lambda self, A, B: len(list(filter(lambda x: x[0] == x[1], zip(A, B))))
	pythagorean = lambda self, A, B: sum(map(lambda i: (i[0] - i[1]) ** 2, list(zip(A, B)))) ** 0.5
	mse = lambda self, A, B: sum(map(lambda x: (x[0] - x[1]) ** 2, zip(A, B))) / len(A)
	lsr = lambda self, x, y: [(sum_xy * len(x) - sum_x * sum_y) / (sum_xx * len(x) - sum_x ** 2) * i + (sum_y - (sum_xy * len(x) - sum_x * sum_y) / (sum_xx * len(x) - sum_x ** 2) * sum_x) / len(x) for i, sum_x, sum_y, sum_xx, sum_xy in [(xi, sum(x), sum(y), sum([xj ** 2 for xj in x]), sum([xj * yj for xj, yj in zip(x, y)])) for xi in x]]
	reshape = lambda self, A, n: [A[i:i + int(len(A) / n)] for i in range(0, len(A), int(len(A) / n))]
	smallest_pair = lambda self, A: min(A, key=lambda sub: abs(sub[1] - sub[0]))
	largest_pair = lambda self, A: max(A, key=lambda sub: abs(sub[1] + sub[0]))
	max_index_values = lambda self, A, B: list(map(max, zip(A, B)))
	percentile = lambda self, A, n: sorted(A)[round((n / 100 * len(A)) - 1)]
	variance = lambda self, A: sum(map(lambda x: (x - sum(A) / len(A)) ** 2, A)) / len(A)
	variance_sample = lambda self, A: sum(map(lambda x: (x - sum(A) / len(A)) ** 2, A)) / ((len(A) - 1) / 1)
	std = lambda self, A: (sum(map(lambda x: (x - sum(A) / len(A)) ** 2, A)) / len(A)) ** 0.5
	std_sample = lambda self, A: (sum(map(lambda x: (x - sum(A) / len(A)) ** 2, A)) / ((len(A) - 1) / 1)) ** 0.5
	cross_sum = lambda self, A, B: list(map(sum, zip(A, B)))
	sort_dict_values = lambda self, A: dict(sorted(A.items(), key=lambda x: x[1], reverse=True))
	sort_list_dicts = lambda self, A, Key: A.sort(key=lambda x: x[Key])
	filter_list_max = lambda self, A, Max: [i for i in A if i <= Max]
	filter_list_min = lambda self, A, Min: [i for i in A if i >= Min]
	zip_lists = lambda self, A, B: list(map(list, zip(A, B)))
	unzip_lists = lambda self, A: list(map(list, zip(*A)))
	combine_lists_str = lambda self, A, B, Sep: list(map(lambda a, b: f"{a}{Sep}{b}", A, B))
	check_prime = lambda self, n: False if int(str(n)[-1]) % 2 == 0 else any([i for i in range(2, int(n ** 0.5) + 1) if n % i == 0]) != True
	find_primes = lambda self, n: [i for i in range(3, n) if (False if int(str(i)[-1]) % 2 == 0 else any([j for j in range(2, int(i ** 0.5) + 1) if i % j == 0]) != True)]
	find_mersenne_prime = lambda self, n: list(filter(lambda i: i is not None, list(map(lambda x: 2 ** x - 1 if self.check_prime(2 ** x - 1) else None, range(1, n + 1)))))
	rot13 = lambda self, word: "".join(list(map(lambda l: chr(((ord(l) - 84) % 26) + 97), word)))
	nested_tuple_it = (lambda self, x: tuple(map(lambda i: self.nested_tuple_it(i) if isinstance(i, list) else i, x)) if isinstance(x, list) else x)
	nested_list_it = (lambda self, x: list(map(lambda i: self.nested_list_it(i) if isinstance(i, tuple) else i, x)) if isinstance(x, tuple) else x)
	factoral = lambda self, n: 1 if n <= 1 else n * self.factoral(n - 1)
	n_divisible_xy = lambda self, n, x, y: all([divmod(n, x)[1] == 0, divmod(n, y)[1] == 0])
	n_odd_below = lambda self, n: len([x for x in range(n) if x % 2 != 0])
	n_even_below = lambda self, n: len([x for x in range(n) if x % 2 == 0])
	remove_outliers = lambda self, A: list(filter(lambda x: (self.mean(A) - 2 * self.std(A)) <= x <= (self.mean(A) + 2 * self.std(A)), A))