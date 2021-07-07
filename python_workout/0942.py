print('Chapter 09 - Exercise 42')
print('Create a FlexibleDict class that ignores the type of index')


class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass

        return dict.__getitem__(self, key)


if __name__ == '__main__':
    fd = FlexibleDict()
    fd['a'] = 100
    print(fd['a'])
    print('------')
    fd[1] = 100
    print(fd[1])
    print('------')
    print(fd['1'])
