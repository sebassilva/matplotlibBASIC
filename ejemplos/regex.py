import re
def regex():
    m = re.search('(?<=abc)media', 'abcdef')
    print(m.group(0))

regex()
