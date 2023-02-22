from collections import OrderedDict
import re


class OrderedDictionary(OrderedDict):
    def __init__(self):
        self._dict = OrderedDict()

    def add(self, item_name, net_price):
        if item_name not in self._dict:
            self._dict[item_name] = int(net_price)
        else:
            self._dict[item_name] += int(net_price)

    def __str__(self):
        return ''.join(['{} {}n'.format(k, v) for k, v in self._dict.items()])


if __name__ == '__main__':
    d = OrderedDictionary()
    for _ in range(int(input())):
        item_name, net_price = input().rsplit(' ', 1)
        d.add(item_name, net_price)

        # if u find n in the string using regex show the new line after the string
    print(re.sub(r'n', r'\n', str(d), flags=re.MULTILINE))
