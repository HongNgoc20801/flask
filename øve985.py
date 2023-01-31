import random


def intro():
    print('''
  ---
  NUMBER SORTING ++
  ---
  RULE:   Nhiệm vụ của trò chơi là sắp xếp 1 dãy số lộn xộn theo thứ tự từ bé đến lớn hoặc từ lớn đến bé.
          Người chơi sẽ được chọn sắp xếp bao nhiêu số trong dãy số
          Đặc biệt: Các số trong dãy sẽ được cho dưới dạng các biểu thức cộng trừ, đòi hỏi chúng ta cần kĩ năng tính toán cực cao nữa đó!
    ''')


def prep(number_sort):
    rawlist1 = []
    rawlist2 = []
    i = 0
    while i < number_sort:
        a = random.randint(1, 60)
        b = random.randint(1, 60)
        options = ["a+b", "a-b", "a*c", "a/c"]
        option = random.choice(options)

        if option == 'a+b' and a + b not in rawlist1:
            rawlist1.append(str(a) + ' + ' + str(b))
            rawlist2.append(a + b)
        elif option == 'a-b' and a - b not in rawlist2:
            rawlist1.append(str(a) + ' - ' + str(b))
            rawlist2.append(a - b)
        elif option == 'a*b ' and a * b not in rawlist2:
            rawlist1.append(str(a) + ' * ' + str(b))
            rawlist2.append(a * b)
        elif option == 'a/b ' and a / b not in rawlist2:
            rawlist1.append(str(a) + ' / ' + str(b))
            rawlist2.append(a / b)
        i = i + 1
        return rawlist1, rawlist2


def sorting(arr, sort_type):
    if sort_type == 0:
        return min(arr)
    else:
        return max(arr)


condition = True
while condition == True:
    intro()
number_guest = int(input('Bạn muốn sắp xếp bao nhiêu số ? >>'))
sort_type = random.randint(0, 1)
raw_list1, raw_list2 = prep(number_guest)
if sort_type == 0:
    print('Sắp xếp dãy số theo thứ tự từ bé đến lớn: ' + str(raw_list1))
else:
    print('Sắp xếp dãy số theo thứ tự từ lớn đến bé: ' + str(raw_list1))

turn = len(raw_list2)
counter = 0
while counter < turn:
    number = sorting(raw_list2, sort_type)
    guess = int(input('Sau khi sắp xếp, số ở vị trí số ' + str(counter + 1) + ' là: >>'))

    if guess == int(number):
        if counter == turn - 1:
            print('Chúc mừng chiến thắng')
        else:
            print('Đúng rồi! Tiếp tục nào!')
    else:
        print('Bạn đã thua, câu trả lời là ' + str(number))
        break
raw_list2.remove(number)
counter = counter + 1
again = input('Bạn có muốn chơi tiếp không? [Y/N]')
if again == 'N':
    condition = False