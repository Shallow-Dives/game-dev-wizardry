import functools

def update_class(context=globals()):
    """Adds all methods and members from the wrapped class to main_class

    Args:
        context (Dict): Pass global context to allow imported use. 
                        Defaults to globals().
    """
    def decorates(context, appended_class):
        exclude=("__module__", "__name__", "__dict__", "__weakref__")
        main_class = context[appended_class.__name__]
        for k, v in appended_class.__dict__.items():
            if k not in exclude:
                setattr(main_class, k, v)
        return main_class

    return functools.partial(decorates, context)
