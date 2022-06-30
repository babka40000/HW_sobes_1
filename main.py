class Stack:
    def __init__(self, volume):
        self.volume = volume

    def isEmpty(self):
        if len(self.volume) == 0:
            return True
        return False

    def push(self, element):
        self.volume.append(element)

    def pop(self):
        res = self.volume[len(self.volume) - 1]
        self.volume.pop()
        return res

    def peek(self):
        return self.volume[len(self.volume) - 1]

    def size(self):
        return len(self.volume)


if __name__ == '__main__':

    template = ['()', '[]', '{}']

    lifo = Stack(list('(((([{}]))))'))

    if lifo.size() % 2 == 0:
        lifo_part_2 = Stack([])

        for i in range(0, int(lifo.size() / 2)):
            lifo_part_2.push(lifo.pop())

        balans = True

        while not lifo.isEmpty():
            if lifo.pop() + lifo_part_2.pop() not in template:
                balans = not balans
                break

        if balans:
            print('Cбалансировано')
        else:
            print('Не сбалансировано')
    else:
        print('Не сбалансировано')
