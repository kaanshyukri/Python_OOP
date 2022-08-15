def tags(text):

    def decorator(func_ref):

        def wrapper(*args):

            return f"<{text}>{func_ref(*args)}</{text}>"

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))

