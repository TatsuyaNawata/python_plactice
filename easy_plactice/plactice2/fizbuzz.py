def fizz_buzz():
    '''
    FizzBuzz拡張版

    1から100までの数字をプリントする。ただし、3の倍数のときは "Fizz"、5の倍数のときは "Buzz"、3と5の倍数のときは "FizzBuzz" を表示する。
    さらに、7の倍数なら "Bazz" を追加する。
    '''
    for i in range(1,101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 7 == 0:
            print("Bazz")
        else:
            print(i)

def reverse_list(lst: list) -> list:
    '''
    リストの要素を逆順に並べ替える関数の作成
    '''
    sorted_list = lst.sort()

def find_max_min(d: dict) -> tuple:
    '''
    辞書内の最大値・最小値を取得する関数
    '''
    max_value = max(d.values())
    min_value = min(d.values())

    return (max_value,min_value)

if __name__ == "__main__":
    test_list = [1,22,3,44,5,6,777,8,9,0,1]
    test_dict = {"apple": 5, "banana": 2, "cherry": 8}
    fizz_buzz()
    reverse_list(test_list)
    m_tuple = find_max_min(test_dict)

    print(test_list)
    print(m_tuple)