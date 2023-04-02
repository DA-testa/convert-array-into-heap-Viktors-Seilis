# python3


def heap(data, a, b, swaps):
    min = a
    left = 2 * a + 1
    right = 2 * a + 2
    if left < b and data[left] < data[min]:
        min = left

    if right < b and data[right] < data[min]:
        min = right
    if a != min:
        swaps.append((a, min))
        data[a], data[min] = data[min], data[a]
        heap(data, min, b, swaps)

def build_heap(data):
    b = len(data)
    swaps = []
    for a in range(b // 2, -1, -1):
        heap(data, a, b, swaps)
    return swaps

def main():
    text= input("Please input I or F :").strip()
    if text == 'I':
        b = int(input("Please input amount of numbers:"))
        d = list(map(int, input("Please input numbers:").split()))
        assert len(d) == b
    elif text  == 'F':
        while True:
            try:
                name = input("Please input file name:")
                with open(f"tests/{name}", "r", encoding="utf-8") as f:
                    a = int(f.readline())
                    d = list(map(int, f.readline().split()))
                    assert len(d) == b
                break
            except FileNotFoundError:
                print("File not found, please enter a valid file name")
    else:
        return
    swaps = build_heap(d)
    print(len(swaps))
    for a, c in swaps:
        print(a, c)
        


if __name__ == "__main__":
    main()
