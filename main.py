# Задание_1
class Stack:
    def __init__(self):
        self.stack_list = []

    def isEmpty_(self):
        if len(self.stack_list) == 0:
            return True
        return False

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        deleted = self.stack_list.pop()
        return deleted

    def peek(self):
        if len(self.stack_list) == 0:
            return None
        last_item = self.stack_list[len(self.stack_list) - 1]
        return last_item

    def size(self):
        return len(self.stack_list)

# Задание_2
def check_balance(list):
    st = Stack()
    open_list = ["(", "{", "["]
    close_list = [")", "}", "]"]
    for item in list:
        if item in open_list:
            st.push(item)
        elif item in close_list and st.size() != 0:
            st.pop()
        elif item not in set(open_list + close_list):
            continue
        else:
            return f'Несбалансированно'
    if st.isEmpty_():
        return f'Сбалансированно'
    else:
        return f'Несбалансированно'


if __name__ == '__main__':
# Проверка работы стека
    st = Stack()
    st.push(1)
    st.push(3)
    st.push(5)
    st.push(7)
    print(st.isEmpty_())
    print(st.stack_list)
    print(st.pop())
    print(st.stack_list)
    print(st.peek())
    print(st.stack_list)
    print(st.size())

# Проверка работы функции
    list_for_check = "[([])((([[[]]])))]{()}"
    print(check_balance(list_for_check))

    list_for_check_2 = "{[([])((([[[]]])))]{()}}"
    print(check_balance(list_for_check_2))
    #
    list_for_check_3 = "[{{{{{{{{{[(])]}}"
    print(check_balance(list_for_check_3))




