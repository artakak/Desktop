def print_func(par):
    print("Hello : ", par)
    return


def on(page_class):
    if page_class in globals().keys():
        print("in if loop")
        page = globals()[page_class]()
        return page
    else:
        print("Page Object: %s does not exist" % page_class)
