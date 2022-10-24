from time import time

def time_solution(input_array, solution):
    start_time = time()
    result = solution(input_array)
    total_time = time() - start_time
    return result, total_time

def get_non_exponential_time_string(input_time):
    return '{0:.10f}'.format(input_time)