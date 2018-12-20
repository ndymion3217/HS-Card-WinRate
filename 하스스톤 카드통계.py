from datetime import datetime
import pickle


class Statistics:
    def __init__(self):
        self.case_list = []

    def make_case(self, string1, string2):
        self.case_list.append(Case(string1, string2))

    def win_rate(self, string, pivot):
        whole_counter = 0
        win_counter = 0
        for i in self.case_list:
            if pivot == 'my_class':
                if i.my_class == string:
                    whole_counter += 1
                    win_counter += 1 if i.w_o_l else 0
            elif pivot == 'whole':
                whole_counter += 1
                win_counter += 1 if i.w_o_l else 0
            elif pivot == "op_class":
                if i.op_class == string:
                    whole_counter += 1
                    win_counter += 1 if i.w_o_l else 0
            elif pivot == 'card_used':
                if i.the_card == string:
                    whole_counter += 1 if i.used else 0
                    win_counter += 1 if i.w_o_l and i.used else 0
            elif pivot == 'card_not_used':
                if i.the_card == string:
                    whole_counter += 1 if i.used is False else 0
                    win_counter += 1 if i.w_o_l and i.used is False else 0
            elif pivot == 'type':
                if i.op_type == string:
                    whole_counter += 1
                    win_counter += 1 if i.w_o_l else 0
        if whole_counter == 0:
            if pivot == 'card_used' or pivot == 'card_not_used' or pivot == 'type':
                return 0, 0
            return 0
        if pivot == 'card_used' or pivot == 'card_not_used' or pivot == 'type':
            return round(win_counter / whole_counter * 100, 2), whole_counter
        return round(win_counter / whole_counter * 100, 2)

    def show_summary(self):
        print('Druid win rate : {} %\nWarlock win rate : {} %\nWarrior win rate : {} %\nRogue win rate : {} %\n'
              'Paladin win rate : {} %\nHunter win rate : {} %\nShaman win rate : {} %\nPriest win rate : {} %\n'
              'Whole game win rate : {} %\nWhole game count : {} games'.format(self.win_rate('드루이드', 'my_class'),
                                                                               self.win_rate('흑마법사', 'my_class'),
                                                                               self.win_rate('전사', 'my_class'),
                                                                               self.win_rate('도적', 'my_class'),
                                                                               self.win_rate('성기사', 'my_class'),
                                                                               self.win_rate('사냥꾼', 'my_class'),
                                                                               self.win_rate('주술사', 'my_class'),
                                                                               self.win_rate('사제', 'my_class'),
                                                                               self.win_rate('', 'whole'),
                                                                               len(self.case_list)))

    def show_versus_statitics(self):
        print('Vs Druid win rate : {} %\nVs Warlock win rate : {} %\nVs Warrior win rate : {} %\n'
              'Vs Rogue win rate : {} %\nVs Paladin win rate : {} %\nVs Hunter win rate : {} %\n'
              'Vs Shaman win rate : {} %\nVs Priest win rate : {} %\nWhole game win rate : {} %\n'
              'Whole game count : {} games'.format(self.win_rate('드루이드', 'op_class'),
                                                   self.win_rate('흑마법사', 'op_class'),
                                                   self.win_rate('전사', 'op_class'),
                                                   self.win_rate('도적', 'op_class'),
                                                   self.win_rate('성기사', 'op_class'),
                                                   self.win_rate('사냥꾼', 'op_class'),
                                                   self.win_rate('주술사', 'op_class'),
                                                   self.win_rate('사제', 'op_class'),
                                                   self.win_rate('', 'whole'),
                                                   len(self.case_list)))
        input()

    def show_type_statistics(self):
        a, b = self.win_rate('어그로덱', 'type')
        c, d = self.win_rate('미드레인지덱', 'type')
        e, f = self.win_rate('컨트롤덱', 'type')
        g, h = self.win_rate('기타덱', 'type')
        print('Vs Aggro deck {} % of {} games\nVs Midrange deck {} % of {} games\nVs Control deck {} % of {} games\n'
              'Vs ETC dexk {} % of {} games'.format(a, b, c, d, e, f, g, h))
        input()

    def show_card_statistics(self):
        card_list = []
        num = 1
        for i in self.case_list:
            if i.the_card not in card_list:
                card_list.append(i.the_card)
        for i in card_list:
            a, b = self.win_rate(i, 'card_used')
            c, d = self.win_rate(i, 'card_not_used')
            print('{}. {} 나왔을때: {} % / {}\n  안나왔을때 {} % / {}'.format(num, i, a, b, c, d))
        input()

    def show_time_statistics(self):
        today = 0
        three = 0
        seven = 0
        month = 0


class Case:
    def __init__(self, string1, string2):
        def character(string):
            if string == '흑':
                return '흑마법사'
            elif string == '전':
                return '전사'
            elif string == '드':
                return '드루이드'
            elif string == '냥':
                return '사냥꾼'
            elif string == '사':
                return '사제'
            elif string == '주':
                return '주술사'
            elif string == '마':
                return '마법사'
            elif string == '성':
                return '성기사'
            else:
                return '도적'

        def deck_type(string):
            if string == '어':
                return '어그로덱'
            elif string == '미':
                return '미드레인지덱'
            elif string == '컨':
                return '컨트롤덱'
            else:
                return '기타덱'
        
        def win_lose(string):
            if string == '승':
                return True
            else:
                return False

        now = datetime.now()
        self.year = now.year
        self.month = now.month
        self.day = now.day
        self.hour = now.hour
        self.minute = now.minute
        self.my_class = character(string1[0])
        self.op_class = character(string1[1])
        self.op_type = deck_type(string1[2])
        self.w_o_l = win_lose(string1[3])
        if string2[0] == '.':
            self.the_card = data.case_list[-1].the_card
        else:
            self.the_card = string2[:-2]
        if string2[1] == '유':
            self.incidence = True
            if string2[2] == '유':
                self.used = True
            else:
                self.used = False
        else:
            self.incidence = False
            self.used = False


def main():
    a = input('내직업, 상대직업,덱분류 승패를 순서대로 쓰세요 : ')
    if a != '.':
        b = input('설정카드는? 그전과같으면 "." 드로유무 사용유무 : ')
        data.make_case(a, b)
    else:
        choice = int(input('1.통계보기 2.케이스보기 3.종료 : '))
        if choice == 1:
            while True:
                data.show_summary()
                choice1 = int(input('1.카드별통계 2.상대직업별통계 3.덱분류별통계 4.시간별통계 5.종료 : '))
                if choice1 == 1:
                    data.show_card_statistics()
                elif choice1 == 2:
                    data.show_versus_statitics()
                elif choice1 == 3:
                    data.show_type_statistics()
                elif choice1 == 4:
                    pass
                elif choice1 == 5:
                    break
                else:
                    pass
        elif choice == 2:
            pass


if __name__ == '__main__':
    try:
        with open('Card_Win_Rate_data.bin', 'rb') as f:
            data = pickle.load(f)
    except:
        data = Statistics()
    main()
    with open('Card_Win_Rate_data.bin', 'wb') as f:
        pickle.dump(data, f)
