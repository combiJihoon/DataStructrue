class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.length = 0

    def size(self):
        return self.length

    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    # 끝에 데이터 삽입
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head

            while node.next:
                node = node.next

            new_node = Node(data)
            node.next = new_node
            new_node.prev = node
            self.tail = new_node

    # present가 가리키는 이전 노드 앞에 새로운 노드 삽입

    def insert_before(self, present, data):
        old = present.prev  # 이전 노드
        new_node = Node(data, old, present)
        # 현재 노드의 이전 노드에 새로운 노드 추가
        present.prev = new_node
        old.next = new_node

        self.length += 1

    # present가 가리키는 다음 노드 앞에 새로운 노드 삽입
    def insert_after(self, present, data):
        old = present.next
        new_node = Node(data, present, old)
        old.prev = new_node
        present.next = new_node

        self.length += 1

    # 노드 n 삭제
    def delete(self, n):
        if self.is_empty():
            return "빈 리스트입니다."

        front = n.prev  # 앞 노드
        rear = n.next  # 뒷 노드
        front.next = rear
        rear.prev = front

        self.length -= 1

        return n.data

    # 데이터 검색 : head부터
    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        while node:
            # 데이터 일치할 경우 True 리턴
            if node.data == data:
                return True
            else:
                node = node.next

        return False

    # 데이터 검색 : tail부터
    def search_from_tail(self, data):
        if self.head == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return True
            else:
                node = node.prev

        return False

    # 리스트 출력
    def get_list(self):
        result = []
        current = self.head

        while current != None:
            result.append(current.data)
            current = current.next

        return result


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

dl = DoublyLinkedList()
dl.insert(node1)
dl.insert(node2)
dl.insert(node3)

print(dl.get_list())
print(dl.search_from_tail(node1))
