class Node:
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None

class Lista:
    def __init__(self):
        self.init = None
        self.tail = None

    def append(self, node):
        """
        Método para inserir um elemento no final
        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def add(self, node):
        """
        Inserir um elemento sempre no inicio da lista
        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

        node.next = self.init
        self.init = node

    def __str__(self):
        str_aux = '['
        node_aux = self.init
        while(node_aux is not None):
            str_aux += str(node_aux.x)
            if(node_aux.next is not None):
                str_aux += ','
            node_aux = node_aux.next
        str_aux += ']'
        return str_aux

if __name__ == '__main__':
    lista = Lista()
    lista.add(Node(x=10))
    lista.add(Node(x=11))
    lista.add(Node(x=12))
    print(lista)
    lista.append(Node(x=7))
    lista.append(Node(x=8))
    lista.append(Node(x=9))
    print(lista)
