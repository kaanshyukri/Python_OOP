def make_bold(func_ref):
    def decorator(*text):

        return f"<b>{func_ref(*text)}</b>"

    return decorator


def make_italic(func_ref):
    def decorator(*text):

        return f"<i>{func_ref(*text)}</i>"

    return decorator


def make_underline(func_ref):
    def decorator(*text):

        return f"<u>{func_ref(*text)}</u>"

    return decorator


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
