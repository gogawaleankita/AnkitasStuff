import sys
import os


# Define and implement bold_tag
def bold_tag(func):
    def inner(args):
        return func("<b>{}</b>".format(args))

    return inner


def say(msg):
    return msg


'''Check the Tail section for input/output'''

if __name__ == "__main__":
    res_lst = list()
    res_lst.append(say(input()))
    print("{}".format(*res_lst))