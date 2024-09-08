import timeit

# Setup code
setup = """
len_longest_substring = 5
current_substring = 'asdfghjkiy'
"""

# max() approach
max_code = """
len_current_substring = len(current_substring)
if len_current_substring > len_longest_substring:
    len_longest_substring = len_current_substring
                """

# Conditional expression approach
conditional_code = "if len(current_substring) > len_longest_substring: len_longest_substring = len(current_substring)"

# Benchmark
max_time = timeit.timeit(max_code, setup=setup, number=1000000)
conditional_time = timeit.timeit(conditional_code, setup=setup, number=1000000)

print(f"max() time: {max_time}")
print(f"Conditional expression time: {conditional_time}")
