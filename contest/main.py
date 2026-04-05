import functools

def array_diff(a: list, b: list) -> list:
    exclude = set(b)
    return [item for item in a if item not in exclude]

def sum_pairs(nums: list, sum: int) -> list:
    seen = set()
    for num in nums:
        target = sum - num
        if target in seen:
            return [target, num]
        seen.add(num)
    return None

def remove_duplicate_ids(obj: dict) -> dict:
    sorted_keys = sorted(obj.keys(), key=int, reverse=True)
    
    seen_elements = set()
    result = {}

    for key in sorted_keys:
        unique_for_key = []
        for char in obj[key]:
            if char not in seen_elements:
                unique_for_key.append(char)
                seen_elements.add(char)
        result[key] = unique_for_key
        
    return result

def lazy(n: int):
    def decorator(func):
        state = {'count': 0}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            state['count'] += 1
            current = state['count']
            
            if n == 1:
                return func(*args, **kwargs)
            if n == -1:
                return None
            
            if n > 1:
                if (current - 1) % n == 0:
                    return func(*args, **kwargs)
                return None
            
            if n < -1:
                period = abs(n)
                if current % period == 0:
                    return None
                return func(*args, **kwargs)
                
            return None
        return wrapper
    return decorator