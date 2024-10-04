def apply_all_func(int_list, *functions):
    results = {}
    for function_name in functions:
        func_result = []
        func_result.append(function_name(int_list))
        results[function_name.__name__] = func_result
    return results
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))