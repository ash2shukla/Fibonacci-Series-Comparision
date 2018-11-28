from timeit import timeit
from functools import partial
import matplotlib.pyplot as plt


fibonacci_list_cache = []
fibonacci_dict_cache = {}

def fibonacci_recursive_none(n=40):
    """
    Fibonacci recursive implementation with Recursion without memoization
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive_none(n - 1) + fibonacci_recursive_none(n - 2)

def fibonacci_recursive(n=40):
    """
    Fiboacci recursive implementation with List for memoization
    """
    if n < len(fibonacci_list_cache):
        return fibonacci_list_cache[n]
    if n == 1:
        calculated_value = 1
    elif n == 2:
        calculated_value = 1
    elif n> 2:
        calculated_value = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    fibonacci_list_cache.append(calculated_value)
    # Lookup can be improved by using dict instead of list
    return calculated_value


def fibonacci_recursive_dict_cache(n=40):
    """
    Fiboacci recursive implementation with Dict for memoization
    """
    if n in fibonacci_dict_cache:
        return fibonacci_dict_cache[n]
    if n == 1:
        calculated_value = 1
    elif n == 2:
        calculated_value = 1
    else:
        calculated_value = fibonacci_recursive_dict_cache(n-1) + fibonacci_recursive_dict_cache(n-2)
    fibonacci_dict_cache[n] = calculated_value
    return calculated_value


def fibonacci_iterative(n=40):
    """
    Fiboacci Iterative implementation
    """
    first = 0
    second = 1
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(2, n+1):
            first, second = second, first + second
        return second


def get_plot_points(pts_count=20):
    fib_dict_points = []
    fib_list_points = []
    fib_iter_points = []
    fib_recr_points = []

    for i in range(1, pts_count):
        print('calling with arg = ', i)
        fib_dict_points.append(timeit(stmt=partial(fibonacci_recursive_dict_cache, n=i)))
        fib_list_points.append(timeit(stmt=partial(fibonacci_recursive, n=i)))
        fib_iter_points.append(timeit(stmt=partial(fibonacci_iterative, n=i)))

        if(i < 8):
            fib_recr_points.append(timeit(stmt=partial(fibonacci_recursive_none, n=i)))

    return fib_dict_points, fib_list_points, fib_iter_points, fib_recr_points

def plot_exec_time():
    fib_dict_points, fib_list_points, fib_iter_points, fib_recr_points = get_plot_points(pts_count=20)

    fib_dict, = plt.plot(fib_dict_points, color='blue')
    fib_list, = plt.plot(fib_list_points, color='skyblue')
    fib_iter, = plt.plot(fib_iter_points, color='olive')
    fib_recr, = plt.plot(fib_recr_points, color='red')
    plt.legend([fib_dict, fib_list, fib_iter, fib_recr], ['Fib_Dict', 'Fib_List', 'Fib_Iter', 'Fib_Recr'])
    plt.show()

if __name__ == "__main__":
    plot_exec_time()
