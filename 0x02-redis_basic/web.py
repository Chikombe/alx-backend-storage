def cache_with_expiration(expiration: int):
    """
    Decorator to cache function results with expiration time.

    Args:
        expiration (int): Expiration time for cached results in seconds.

    Returns:
        function: Decorator function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            url = args[0]
            key = f"cache:{url}"
            if key in cache:
                count, timestamp = cache[key]
                if time.time() - timestamp > expiration:
                    # Cache expired, remove the entry from cache
                    del cache[key]
                    result = func(*args, **kwargs)
                    cache[key] = (result, time.time())  # Cache the new result
                    return result
                else:
                    # Cache still valid, return cached result
                    return cache[key][0]
            else:
                # URL not cached, fetch and cache the result
                result = func(*args, **kwargs)
                cache[key] = (result, time.time())
                return result
        return wrapper
    return decorator
