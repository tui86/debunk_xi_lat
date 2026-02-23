import itertools
import matplotlib.pyplot as plt
import random

class BlackJack:

    def profile(self):
        deck = [2,2,2,2, 
                3,3,3,3, 
                4,4,4,4, 
                5,5,5,5, 
                6,6,6,6, 
                7,7,7,7, 
                8,8,8,8, 
                9,9,9,9, 
                10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10, 
                "A","A","A","A"]
        quanlity = 52

        return deck, quanlity
    
    def convert_A(self, hand: list):
        if 'A' not in hand:
            return sum(hand)
        point = 0
        number_of_A = hand.count('A')
        for card in hand:
            if card != "A":
                point += card
        for i in range(number_of_A):
            if point + 11 <= 21:
                point += 11
            elif point + 10 <= 21:
                point += 10
            else:
                point += 1
        return point
    
    def is_black_jack(self, hand:list):
        if 10 in hand and "A" in hand:
            return 1
        elif hand == ['A', 'A']:
            return 2
        else:
            return 0
        
    def draw_card(self, hand_player:list, hand_dealer:list, permuatations_deck:list, ultis:int = 17):
        for i in range(len(hand_player)):
            while self.convert_A(hand_player[i]) < ultis and len(hand_player[i]) < 5:
                hand_player[i].append(permuatations_deck.pop(0))
        while self.convert_A(hand_dealer) < ultis and len(hand_dealer) < 5:
            hand_dealer.append(permuatations_deck.pop(0))

    #Hàm sẽ quét tất cả các biến có sẵn, đừng sử dụng.
    def all_combo(self, player:int = 1, vizualize: bool = False):
        deck, quantity = self.profile()

        case_4 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_5 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_6 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_7 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_8 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_9 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_10 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_11 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_12 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_13 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_14 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_15 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_16 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_17 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_18 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_19 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_20 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        case_21 =  {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "dilinh": 0,
        "hand_dealer": [],
        'hand_player': []
        }

        AK = {
        "win": 0,
        "draw": 0,
        "loss": 0,
        "hand_player": [],
        }

        AA = {
            "win": 0,
            "draw": 0,
            "hand_player": [],
        }

        player_hand = [[] for _ in range(player)]
        dealer_hand = []
        turns = 0

        for terms in itertools.permutations(deck, 5+player*5):
            win = 0
            loss = 0
            terms = list(terms)
            for _ in range(2):
                for i in range(player):
                    player_hand[i].append(terms.pop(0))
                dealer_hand.append(terms.pop(0))
            player_is_black_jack = []

            for hand in player_hand:
                player_is_black_jack.append(self.is_black_jack(hand))
            
            dealer_is_black_jack = self.is_black_jack(dealer_hand)
            

            if dealer_is_black_jack > 0:
                for point in player_is_black_jack:
                    if point > dealer_is_black_jack:
                        loss+=1
                        player_hand.pop(0)
                    elif point < dealer_is_black_jack:
                        win+=1
                        player_hand.pop(0)
                    else:
                        player_hand.pop(0)

            if not player_hand:
                if win > loss:
                    if dealer_is_black_jack == 1:
                        AK["win"]+=1
                        AK["hand_player"].append(player_hand)
                    elif dealer_is_black_jack == 2:
                        AA["win"]+=1
                        AA["hand_player"].append(player_hand)
                elif win < loss:
                    if dealer_is_black_jack == 1:
                        AK["loss"]+=1
                        AK["hand_player"].append(player_hand)
                elif win == loss:
                    if dealer_is_black_jack == 1:
                        AK["draw"]+=1
                        AK["hand_player"].append(player_hand)
                    elif dealer_is_black_jack == 2:
                        AA["draw"]+=1
                        AA["hand_player"].append(player_hand)
                turns+=1
                continue

            player_point = []

            for hand in player_hand:
                player_point.append(self.convert_A(hand))
            
            dealer_point = self.convert_A(dealer_hand)
            
            match dealer_point:
                case 4:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_4["win"]+=1
                    elif win < loss:
                        case_4["loss"]+=1
                    elif win == loss:
                        case_4["draw"]+=1
                    case_4["hand_dealer"].append(dealer_hand)
                    case_4["hand_player"].append(player_hand)

                case 5:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_5["win"]+=1
                    elif win < loss:
                        case_5["loss"]+=1
                    elif win == loss:
                        case_5["draw"]+=1
                    case_5["hand_dealer"].append(dealer_hand)
                    case_5["hand_player"].append(player_hand)

                case 6:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_6["win"]+=1
                    elif win < loss:
                        case_6["loss"]+=1
                    elif win == loss:
                        case_6["draw"]+=1
                    case_6["hand_dealer"].append(dealer_hand)
                    case_6["hand_player"].append(player_hand)

                case 7:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_7["win"]+=1
                    elif win < loss:
                        case_7["loss"]+=1
                    elif win == loss:
                        case_7["draw"]+=1
                    case_7["hand_dealer"].append(dealer_hand)
                    case_7["hand_player"].append(player_hand)

                case 8:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_8["win"]+=1
                    elif win < loss:
                        case_8["loss"]+=1
                    elif win == loss:
                        case_8["draw"]+=1
                    case_8["hand_dealer"].append(dealer_hand)
                    case_8["hand_player"].append(player_hand)

                case 9:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_9["win"]+=1
                    elif win < loss:
                        case_9["loss"]+=1
                    elif win == loss:
                        case_9["draw"]+=1
                    case_9["hand_dealer"].append(dealer_hand)
                    case_9["hand_player"].append(player_hand)

                case 10:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_10["win"]+=1
                    elif win < loss:
                        case_10["loss"]+=1
                    elif win == loss:
                        case_10["draw"]+=1
                    case_10["hand_dealer"].append(dealer_hand)
                    case_10["hand_player"].append(player_hand)

                case 11:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_11["win"]+=1
                    elif win < loss:
                        case_11["loss"]+=1
                    elif win == loss:
                        case_11["draw"]+=1
                    case_11["hand_dealer"].append(dealer_hand)
                    case_11["hand_player"].append(player_hand)

                case 12:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_12["win"]+=1
                    elif win < loss:
                        case_12["loss"]+=1
                    elif win == loss:
                        case_12["draw"]+=1
                    case_12["hand_dealer"].append(dealer_hand)
                    case_12["hand_player"].append(player_hand)

                case 13:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_13["win"]+=1
                    elif win < loss:
                        case_13["loss"]+=1
                    elif win == loss:
                        case_13["draw"]+=1
                    case_13["hand_dealer"].append(dealer_hand)
                    case_13["hand_player"].append(player_hand)

                case 14:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_14["win"]+=1
                    elif win < loss:
                        case_14["loss"]+=1
                    elif win == loss:
                        case_14["draw"]+=1
                    case_14["hand_dealer"].append(dealer_hand)
                    case_14["hand_player"].append(player_hand)

                case 15:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_15["win"]+=1
                    elif win < loss:
                        case_15["loss"]+=1
                    elif win == loss:
                        case_15["draw"]+=1
                    case_15["hand_dealer"].append(dealer_hand)
                    case_15["hand_player"].append(player_hand)

                case 16:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_16["win"]+=1
                    elif win < loss:
                        case_16["loss"]+=1
                    elif win == loss:
                        case_16["draw"]+=1
                    case_16["hand_dealer"].append(dealer_hand)
                    case_16["hand_player"].append(player_hand)

                case 17:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_17["win"]+=1
                    elif win < loss:
                        case_17["loss"]+=1
                    elif win == loss:
                        case_17["draw"]+=1
                    case_17["hand_dealer"].append(dealer_hand)
                    case_17["hand_player"].append(player_hand)

                case 18:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_18["win"]+=1
                    elif win < loss:
                        case_18["loss"]+=1
                    elif win == loss:
                        case_18["draw"]+=1
                    case_18["hand_dealer"].append(dealer_hand)
                    case_18["hand_player"].append(player_hand)

                case 19:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_19["win"]+=1
                    elif win < loss:
                        case_19["loss"]+=1
                    elif win == loss:
                        case_19["draw"]+=1
                    case_19["hand_dealer"].append(dealer_hand)
                    case_19["hand_player"].append(player_hand)

                case 20:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_20["win"]+=1
                    elif win < loss:
                        case_20["loss"]+=1
                    elif win == loss:
                        case_20["draw"]+=1
                    case_20["hand_dealer"].append(dealer_hand)
                    case_20["hand_player"].append(player_hand)

                case 21:
                    self.draw_card(player_hand, dealer_hand, terms)
                    if dealer_point > 21:
                        for point in player_point:
                            if point <= 21:
                                win+=1
                    else:
                        for point in player_point:
                            if point > dealer_point and point <=21:
                                loss+=1
                            elif point < dealer_point or point > 21:
                                win+=1
                    if win > loss:
                        case_21["win"]+=1
                    elif win < loss:
                        case_21["loss"]+=1
                    elif win == loss:
                        case_21["draw"]+=1
                    case_21["hand_dealer"].append(dealer_hand)
                    case_21["hand_player"].append(player_hand)
            turns+=1
        # Vẽ biểu đồ cột chồng
        if vizualize:
            labels = ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
            win_counts = [case_4["win"], case_5["win"], case_6["win"], case_7["win"], case_8["win"], case_9["win"], case_10["win"], case_11["win"], case_12["win"], case_13["win"], case_14["win"], case_15["win"], case_16["win"], case_17["win"], case_18["win"], case_19["win"], case_20["win"], case_21["win"]]
            draw_counts = [case_4["draw"], case_5["draw"], case_6["draw"], case_7["draw"], case_8["draw"], case_9["draw"], case_10["draw"], case_11["draw"], case_12["draw"], case_13["draw"], case_14["draw"], case_15["draw"], case_16["draw"], case_17["draw"], case_18["draw"], case_19["draw"], case_20["draw"], case_21["draw"]]
            loss_counts = [case_4["loss"], case_5["loss"], case_6["loss"], case_7["loss"], case_8["loss"], case_9["loss"], case_10["loss"], case_11["loss"], case_12["loss"], case_13["loss"], case_14["loss"], case_15["loss"], case_16["loss"], case_17["loss"], case_18["loss"], case_19["loss"], case_20["loss"],case_21['loss']]

            x = range(len(labels))
            plt.bar(x, win_counts, label='Win')
            plt.bar(x, draw_counts, bottom=win_counts, label='Draw')
            plt.bar(x, loss_counts, bottom=[i+j for i,j in zip(win_counts, draw_counts)], label='Loss')

            plt.xlabel('Dealer Point')
            plt.ylabel('Count')
            plt.title('Win/Draw/Loss Counts by Dealer Point')
            plt.xticks(x, labels)
            plt.legend()
            plt.show()

        return case_4, case_5, case_6, case_7, case_8, case_9, case_10, case_11, case_12, case_13, case_14, case_15, case_16, case_17, case_18, case_19, case_20, case_21, AK, AA

    def Monto_carlo_black_jack(self, player: int = 1, turns:int = 1000000, vizualize: bool = False, ultis:int = 17):
        #Lấy khoá là dealer
        deck, quantity = self.profile()
        case_point = {i: {'loss': 0, 'draw': 0, 'win': 0} for i in range(4, 22)}
        AK = {'loss': 0, 'draw': 0, 'win': 0}
        AA = {'loss': 0, 'draw': 0, 'win': 0}
        net = 0
        for _ in range(turns):
            flag_player = [False for _ in range(player)]
            win = 0
            loss = 0
            terms = random.sample(deck, quantity)
            player_hand = [[] for _ in range(player)]
            dealer_hand = []
            for i in range(2):
                for j in range(player):
                    player_hand[j].append(terms.pop(0))
                dealer_hand.append(terms.pop(0))
            player_is_black_jack = []

            for hand in player_hand:
                player_is_black_jack.append(self.is_black_jack(hand))
            
            dealer_is_black_jack = self.is_black_jack(dealer_hand)
            

            if dealer_is_black_jack > 0 or any(True for i in player_is_black_jack if i > 0):
                count = -1
                for hand, point in zip(player_hand, player_is_black_jack):
                    count+=1
                    if point > dealer_is_black_jack:
                        loss+=1
                        net-=1
                        flag_player[count] = True
                    elif point < dealer_is_black_jack:
                        win+=1
                        net+=1
                        flag_player[count] = True
                    elif point == dealer_is_black_jack:
                        flag_player[count] = True

            if all(flag_player):
                if win > loss:
                    if dealer_is_black_jack == 1:
                        AK["win"]+=1
                    elif dealer_is_black_jack == 2:
                        AA["win"]+=1
                elif win < loss:
                    if dealer_is_black_jack == 1:
                        AK["loss"]+=1
                elif win == loss:
                    if dealer_is_black_jack == 1:
                        AK["draw"]+=1
                    elif dealer_is_black_jack == 2:
                        AA["draw"]+=1
                continue

            player_point = []

            for hand in player_hand:
                player_point.append(self.convert_A(hand))
            
            dealer_start_point = self.convert_A(dealer_hand)
            self.draw_card(player_hand, dealer_hand, terms, ultis)
            dealer_point = self.convert_A(dealer_hand)
            for hand in player_hand:
                player_point = self.convert_A(hand)
                #Xử lí khi dealer hoặc player được ngũ linh
                dealer_5 = len(dealer_hand) == 5 and dealer_point <= 21
                player_5 = len(hand) == 5 and player_point <= 21
                if dealer_5 or player_5:
                    if dealer_5 and not player_5:
                        win+=1
                        net+=1
                    elif not dealer_5 and player_5:
                        loss+=1
                        net-=1
                    
                    # nếu cả 2 đều ngũ linh thì tính điểm để phân thắng thua, ai cao điểm hơn thì thua, ai thấp điểm hơn thì thắng, nếu điểm bằng nhau thì hoà
                    if dealer_5 and player_5:
                        if dealer_point < player_point:
                            win+=1
                            net+=1
                        elif dealer_point > player_point:
                            loss+=1
                            net-=1
                    
                    continue


                if dealer_point < 22:
                    if player_point > dealer_point and player_point <= 21:
                        loss+=1
                        net-=1
                    elif player_point < dealer_point or player_point > 21:
                        win+=1
                        net+=1
                else:
                    if player_point <= 21:
                        loss+=1
                        net-=1
            if win > loss:
                case_point[dealer_start_point]['win']+=1
            elif win < loss:
                case_point[dealer_start_point]['loss']+=1
            else:
                case_point[dealer_start_point]['draw']+=1
        #Vẽ biểu đồ cột chồng
        labels = [str(i) for i in range(4, 22)]
        labels.append("AK")
        labels.append("AA")
        win_percent = [case_point[i]['win'] / (case_point[i]['win'] + case_point[i]['draw'] + case_point[i]['loss']) *100 if (case_point[i]['win'] + case_point[i]['draw'] + case_point[i]['loss']) > 0 else 0 for i in range(4, 22)]
        draw_percent = [case_point[i]['draw'] / (case_point[i]['win'] + case_point[i]['draw'] + case_point[i]['loss']) *100 if (case_point[i]['win'] + case_point[i]['draw'] + case_point[i]['loss']) > 0 else 0 for i in range(4, 22)]
        loss_percent = [case_point[i]['loss'] / (case_point[i]['win'] + case_point[i]['draw'] + case_point[i]['loss']) *100 if (case_point[i]['win'] + case_point[i]['draw'] + case_point[i]['loss']) > 0 else 0 for i in range(4, 22)]
        win_percent.append(AK["win"] / (AK["win"] + AK["draw"] + AK["loss"]) *100 if (AK["win"] + AK["draw"] + AK["loss"]) > 0 else 0)
        win_percent.append(AA["win"] / (AA["win"] + AA["draw"] + AA["loss"]) *100 if (AA["win"] + AA["draw"] + AA["loss"]) > 0 else 0)
        draw_percent.append(AK["draw"] / (AK["win"] + AK["draw"] + AK["loss"]) *100 if (AK["win"] + AK["draw"] + AK["loss"]) > 0 else 0)
        draw_percent.append(AA["draw"] / (AA["win"] + AA["draw"] + AA["loss"]) *100 if (AA["win"] + AA["draw"] + AA["loss"]) > 0 else 0)
        loss_percent.append(AK["loss"] / (AK["win"] + AK["draw"] + AK["loss"]) *100 if (AK["win"] + AK["draw"] + AK["loss"]) > 0 else 0)
        loss_percent.append(AA["loss"] / (AA["win"] + AA ["draw"] + AA ["loss"]) *100 if (AA ["win"] + AA ["draw"] + AA ["loss"]) > 0 else 0)
        total_win = sum(case_point[i]['win'] for i in range(4,22)) + AK['win'] + AA['win']
        total_draw = sum(case_point[i]['draw'] for i in range(4,22)) + AK['draw'] + AA['draw']
        total_loss = sum(case_point[i]['loss'] for i in range(4,22)) + AK['loss'] + AA['loss']

        total_round = total_win + total_draw + total_loss

        print("Win rate:", total_win / total_round * 100)
        print("Draw rate:", total_draw / total_round * 100)
        print("Loss rate:", total_loss / total_round * 100)
        print("Net profit per round:", net/total_round * 100, '%')
        if vizualize:    
            x = range(len(labels))
            plt.bar(x, win_percent, label='Win')
            plt.bar(x, draw_percent, bottom=win_percent, label='Draw')
            plt.bar(x, loss_percent, bottom=[i+j for i,j in zip(win_percent, draw_percent)], label='Loss')

            plt.xlabel('Dealer Starting Point')
            plt.ylabel('Count')
            plt.title('Thắng/ Hoà/ Thua theo góc nhìn của Dealer')
            plt.xticks(x, labels)
            plt.legend()
            plt.show()



        return {
            'case_point': case_point,
            'AK': AK,
            'AA': AA,
            'net': net/total_round * 100,
            'win_rate': total_win / total_round * 100,
            'draw_rate': total_draw / total_round * 100,
            'loss_rate': total_loss / total_round * 100
        }
    
    def combat1vs1(self, capital:int = 100000, bet:int = 10000, target:int = 200000, vizualize: bool = False, ultis:int = 17):
        deck, quantity = self.profile()
        capital_per_turn = [capital]
        while capital > 0 and capital > bet and capital < target:
            player_hand = []
            dealer_hand = []
            terms = random.sample(deck, quantity)
            for i in range(2):
                player_hand.append(terms.pop(0))
                dealer_hand.append(terms.pop(0))

            player_is_black_jack = self.is_black_jack(player_hand)
            dealer_is_black_jack = self.is_black_jack(dealer_hand)

            # xử lý blackjack
            if dealer_is_black_jack > 0 or player_is_black_jack > 0:
                if player_is_black_jack > dealer_is_black_jack:
                    capital += bet
                elif player_is_black_jack < dealer_is_black_jack:
                    capital -= bet
                capital_per_turn.append(capital)
                continue

            # không phải blackjack: rút tiếp theo chiến thuật
            dealer_start_point = self.convert_A(dealer_hand)
            self.draw_card([player_hand], dealer_hand, terms, ultis)
            # cập nhật điểm sau khi rút
            player_point = self.convert_A(player_hand)
            dealer_point = self.convert_A(dealer_hand)

            # Ngũ linh
            dealer_5 = len(dealer_hand) == 5 and dealer_point <= 21
            player_5 = len(player_hand) == 5 and player_point <= 21
            if dealer_5 or player_5:
                if dealer_5 and not player_5:
                    capital -= bet
                elif not dealer_5 and player_5:
                    capital += bet

                # nếu cả 2 đều ngũ linh thì dealer thấp hơn sẽ thắng (theo yêu cầu)
                if dealer_5 and player_5:
                    if dealer_point < player_point:
                        capital -= bet
                    elif dealer_point > player_point:
                        capital += bet

                capital_per_turn.append(capital)
                continue

            # so sánh điểm thông thường
            if dealer_point < 22:
                if player_point > dealer_point and player_point <= 21:
                    capital += bet
                elif player_point < dealer_point or player_point > 21:
                    capital -= bet
            else:
                if player_point <= 21:
                    capital += bet

            capital_per_turn.append(capital)

        if vizualize:
            plt.plot(capital_per_turn, label='Capital per turn')
            plt.title('Capital per turn')
            plt.xlabel('Turn')
            plt.ylabel('Capital')
            plt.legend()
            plt.show()
        
        return capital >= target


                        

