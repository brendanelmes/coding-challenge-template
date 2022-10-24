import pytest
import logging
from utils.timer import time_solution, get_non_exponential_time_string
from solutions.solution1 import solution1
from solutions.solution2 import solution2

LOGGER = logging.getLogger(__name__)

solutions = [solution1,solution2]

params = {
    'empty_array': ([],1),
    'short_array': ([1,2,3],3),
    'worst_case': ([1]*1000000,1000000)
}

@pytest.mark.parametrize('test_input,expected', list(params.values()), ids=list(params.keys()))
def test_multiple_solutions(test_input, expected):
    solution_id = 1
    for solution in solutions:
        result, end = time_solution(test_input, solution)
        LOGGER.info('Solution{}: '.format(solution_id) + get_non_exponential_time_string(end))
        solution_id += 1
        assert result == expected