class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print('==================================')
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)
        print('==================================')


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


def set_contact():
    name = input('name: ')
    phone_number = input('phone number:')
    e_mail = input('email :')
    addr = input('address:')
    contact = Contact(name, phone_number, e_mail, addr)
    return contact


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def store_contact(contact_list):
    f = open('contact_db.txt', 'wt')
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()


def load_contact(contact_list):
    f = open('contact_db.txt', 'rt')
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()

# load_contact 함수는 먼저 readlines 함수를 이용해 파일에 있는 모든 데이터를 읽습니다.
# 연락처 하나당 4줄의 데이터가 존재하므로 파일에서 읽어 들인 전체 라인 수를 4로 나누어 몇 개의 데이터가 존재하는지 확인합니다.
# 나눗셈 연산을 수행하면 num 값이 실수가 되는데, 이 값을 int 내장 함수를 사용해 정수형으로 형변환합니다.
# for 문에서는 num의 개수만큼 루프를 돌면서 lines 리스트에 저장된 데이터를 읽어 들여 Contact 클래스의 인스턴스를 생성하고 생성한 인스턴스를 contact_list에 추가합니다.
# 앞서 설명한 것처럼 파일로 저장된 연락처를 불러오는 것은 연락처 관리 프로그램이 실행될 때 이뤄져야 합니다.
# 따라서 다음과 같이 run 함수가 시작하는 부분에서 load_contact 함수를 호출하면 됩니다.


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu = input('메뉴 선택 : ')
    return int(menu)


def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input('name: ')
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
            break

    # kim = Contact('김일구', '010-8812-1193', 'ilgu.kim@python.com', 'Seoul')
    # kim.print_info()


if __name__ == "__main__":
    run()
