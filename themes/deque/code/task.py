def length(head):
    pointers = {head}           # множество: проверка "in" за O(1), а не O(n) как у списка

    head = head.next
    answer = 1
    while head not in pointers:
        pointers.add(head)
        head = head.next
        answer += 1
    return answer # --> возвращает длину массива
