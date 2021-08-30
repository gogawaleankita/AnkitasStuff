import os
import re

# Enter your code here
sample_text = ['199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245',
               'unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
               '199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085',
               'burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0',
               '199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 4179',
               'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0',
               'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0',
               '205.212.115.106 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985',
               'd104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
               '129.94.144.152 - - [01/Jul/1995:00:00:13 -0400] "GET / HTTP/1.0" 200 7074',
               'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',
               'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786',
               'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204',
               'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',
               'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786'];


def findPattern(pattern, givenList):
    arr = list();
    for i in range(len(givenList)):
        arr.append(re.search(pattern, givenList[i], re.M | re.I).group(0))
    return arr;


def func1():
    pattern = r'[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]+';
    hosts = findPattern(pattern, sample_text);

    print(hosts)


def func2():
    timestamps = findPattern(r'[0-9][0-9]/[a-zA-z]+/[0-9]+:[0-9]+:[0-9]+:[0-9]+\s-[0-9]+', sample_text);

    # 01/Jul/1995:00:00:14 -0400
    print(timestamps)


def func3():
    # mypat=findPattern(pattern,sample_text);
    finalList = findPattern(r'GET.*/[0-9].[0-9]+', sample_text);
    method_uri_protocol = list();
    for i in range(len(finalList)):
        method_uri_protocol.append(tuple(re.split(" ", finalList[i])))

    print(method_uri_protocol)


def func4():
    status1 = findPattern(r'"\s[0-9]+', sample_text);
    status = findPattern(r'[0-9]+', status1);
    print(status)


def func5():
    content_size = findPattern(r'[0-9]+$', sample_text);
    content_size = findPattern(r'[0-9]+$', sample_text);

    print(content_size)
    '''For testing the code, no input is to be provided'''


func1()

func2();
func3();
func4();
func5();

