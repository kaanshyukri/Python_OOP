def type_check(type_info):
    def decorator(func_ref):

        def wrapper(info):

            if isinstance(info, type_info):
                return func_ref(info)
            return f"Bad Type"

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

