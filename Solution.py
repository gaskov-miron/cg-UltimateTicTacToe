import sys
import numpy as np
import copy
import random


t = '483-467|347-599|363-590|218-764|487-513|207-734|494-506|N460-503|410-459|299-657|188-812|347-529|499-501|230-729|271-685|130-870|372-628|183-817|N323-556|389-563|238-762|398-511|521-479|300-700|742-258|482-518|323-677|505-436|661-339|310-690|X318-651|214-786|401-526|189-754|118-882|258-742|441-542|250-750|621-337|123-877|326-674|N257-743|106-809|292-619|616-305|212-649|X110-890|117-883|90-823|267-733|130-870|521-479|115-885|125-875|131-869|145-855|N128-872|109-891|138-862|57-765|293-675|234-766|524-476|255-745|240-760|246-754|503-497|245-755|X478-458|219-622|738-262|310-690|119-881|513-487|235-765|N522-478|342-590|121-757|519-481|484-439|375-625|758-242|255-620|263-737|507-493|674-242|301-495|X254-746|150-850|339-661|239-742|129-871|309-654|355-645|238-762|495-505|151-849|249-751|N251-749|219-781|265-735|501-499|379-552|X472-484|224-595|724-215|379-504|149-721|630-282|466-443|760-240|99-811|537-463|N501-499|180-630|375-384|314-443|NNNNNNNNNNNNNNNNNX358-527|132-698|609-332|248-752|137-863|488-512|446-435|131-631|741-259|260-740|129-871|524-476|245-755|N503-497|229-771|116-752|525-475|459-428|135-615|760-240|198-598|137-739|519-481|553-241|115-509|X502-498|298-702|710-290|447-521|248-752|614-330|766-234|470-530|733-267|250-750|488-512|N490-510|502-498|500-500|848-152|753-117|X216-780|125-875|330-670|152-848|N304-696|309-672|261-739|352-648|512-488|235-765|336-478|260-740|523-477|629-323|239-672|X125-849|N259-676|259-741|N386-614|231-769|N378-425|491-509|N391-609|384-616|394-606|511-489|474-526|NNNNNNNNN395-531|261-739|571-314|255-745|250-750|230-770|643-357|251-749|XNNNNNN240-760|N494-506|243-757|N257-743|483-517|NXNNN510-490|239-569|566-241|136-647|241-759|125-510|615-239|255-489|X470-514|261-739|642-358|330-670|N626-374|663-308|535-465|766-234|240-687|N491-361|489-511|N765-235|739-261|764-236|741-259|52-823|446-490|125-733|0-891|254-616|419-540|237-763|655-345|108-892|248-752|117-883|N260-740|265-735|255-745|257-743|64-696|608-249|129-601|0-750|222-491|625-375|264-736|XN309-691|123-843|N257-685|251-749|N524-476|123-877|N262-738|131-869|N256-744|245-755|N253-747|259-741|N507-493|126-819|N262-622|488-512|NX131-612|443-476|120-665|0-766|245-578|442-470|248-516|635-365|148-822|149-851|236-764|127-873|N248-752|239-761|224-776|260-740|399-415|116-415|651-174|127-461|0-512|241-358|617-201|263-324|X0-902|265-735|0-911|0-946|0-854|242-758|0-863|505-495|NNNNNNNN0-785|516-484|0-815|0-873|0-769|484-516|0-756|XNNNNNNNNNNNNNNNNNNNNNNNNNX0-796|239-620|0-789|0-873|0-759|241-653|0-746|492-508|NNNNNNNNN261-448|0-616|504-241|0-626|0-748|0-479|491-267|0-485|X242-758|609-391|245-600|0-830|511-375|652-279|507-493|784-216|242-758|477-523|242-758|N494-506|542-458|481-519|521-479|130-649|743-257|271-426|0-622|484-269|720-280|508-492|XN623-377|238-708|N520-344|504-496|N756-244|256-744|N484-516|252-748|N498-502|496-504|N513-487|378-622|N745-255|237-631|N498-256|505-495|NX242-451|633-367|260-502|0-603|479-399|628-250|499-260|748-252|310-623|276-724|450-550|258-742|N511-489|489-511|501-499|492-508|240-263|753-247|242-246|0-250|484-246|764-236|490-251|X304-696|241-759|550-450|551-449|304-696|700-300|247-753|345-655|N350-650|392-608|264-736|379-621|492-508|736-264|507-493|570-230|767-233|502-498|XN258-742|N358-462|339-661|N700-300|N328-611|119-820|N264-609|263-737|N375-625|515-485|N759-241|484-516|N494-248|483-517|NX624-376|628-372|499-501|612-388|691-309|635-365|739-261|527-473|487-513|500-500|503-497|N492-508|495-505|501-499|501-499|766-234|756-244|739-261|744-256|751-249|740-260|773-227|X247-753|250-750|260-740|358-642|256-744|510-490|NNNNNNN484-516|750-250|509-491|503-497|739-261|494-506|XN240-760|N228-772|234-766|N480-520|NNNNNNNN523-477|N741-259|497-503|N510-490|484-516|NX251-749|242-758|270-730|248-752|376-624|239-761|500-500|NNNNNNNNN487-513|721-279|469-531|496-504|482-518|771-229|464-536|X512-488|477-523|749-251|740-260|475-525|723-277|496-504|734-266|N731-269|736-264|510-490|739-261|469-531|743-257|513-487|760-240|762-238|496-504|XN254-626|N494-243|504-496|N748-252|N601-270|273-596|N502-254|495-505|N747-253|N733-267|517-483|N490-242|513-487|NXXXXXXXXXXXXNXXXXXXXXXXXX209-791|121-879|344-656|265-735|128-818|502-498|0-930|271-729|N231-769|0-859|237-763|507-493|375-625|X512-488|132-506|756-244|0-829|498-502|274-726|N503-497|174-635|0-624|497-503|235-529|764-236|314-629|264-611|490-510|239-373|XNNNNNNNNNNNNNNX388-437|0-599|746-254|0-874|550-450|NNN267-733|0-765|515-485|0-743|532-468|NNN497-239|0-489|X439-561|256-744|605-395|497-503|250-612|751-249|0-892|510-490|N510-490|0-732|485-515|763-237|776-224|X235-362|774-226|0-751|510-490|258-742|N500-500|0-497|506-494|492-263|785-215|629-242|494-240|749-251|517-217|X474-526|476-524|486-514|735-265|N494-506|491-363|743-257|754-246|509-491|XNNN0-882|495-505|NN0-753|484-516|495-505|NXXXNXXXXXX0-937|255-745|N235-765|0-865|239-761|0-804|478-522|0-892|238-762|0-723|X114-886|N253-747|118-882|N249-751|N493-507|126-874|N246-754|526-474|NX101-795|0-733|247-753|0-631|473-527|136-745|0-759|263-737|504-496|0-520|XNNNNNN0-885|509-491|NN0-771|XNNNNNNNNNNNNNXNNN0-739|500-500|NNN500-500|0-499|X0-862|504-496|N524-476|0-753|492-508|0-741|501-499|0-729|484-516|0-765|X247-753|N487-513|252-748|N508-492|N509-491|248-752|N524-476|501-499|NX226-512|0-493|481-519|0-482|482-518|229-496|0-485|537-463|0-514|X262-738|256-744|N253-747|249-751|243-757|486-514|505-495|485-515|504-496|XN245-755|N268-732|141-859|N235-765|N524-476|477-523|N469-531|505-495|512-488|N519-481|481-519|496-504|500-500|512-488|503-497|NNNNNN484-516|495-505|NN495-505|XNNNNNNNN509-491|NN483-517|NXNNNNNNNN507-493|512-488|NNN485-515|X473-527|472-528|N504-496|495-505|479-521|N487-513|N494-506|237-763|N477-523|XXXNXXXX489-443|750-250|495-505|494-506|504-380|X500-500|505-495|480-520|545-455|X511-248|X0-867|484-516|NN0-759|XNNNNX0-523|XXXXXXXXXXXXXX243-757|N510-490|244-264|624-0|N274-479|122-121|0-238|N0-750|484-516|NN0-476|524-0|0-766|0-503|NN0-257|0-496|0-0|0-762|XNX0-496|X113-887|132-868|N133-867|250-750|257-743|498-502|66-540|XN0-880|N248-752|N501-499|N0-626|NX239-761|251-749|266-734|254-746|106-515|254-746|XNNNNNN502-498|0-621|XNNNNN516-484|N0-757|NXNNN487-513|N0-492|NX256-744|235-765|N235-765|493-507|537-463|126-529|XN0-735|N500-500|NN0-474|NX497-503|521-479|493-507|502-498|502-498|485-515|XNNNNNN531-469|0-747|XNNNNNN123-761|504-496|0-763|0-500|261-739|XNNNNNNNNXNNNNNNN475-525|N0-496|NXNNNNNN496-504|0-519|XNNNNNN274-481|0-482|0-513|513-487|X494-506|482-518|N502-498|495-505|499-501|507-493|XNNNNNN0-496|XXXNXXXXX499-501|506-494|483-517|520-359|507-493|X491-509|XNNNN0-739|NXNXXXXXXXNNNNN520-480|518-482|505-495|517-483|XXNXN489-511|497-503|NNNNNNNNNXXNXNXNNXNXNNNNNXXXXX136-114|N0-245|251-496|471-529|0-242|N0-510|N0-0|N0-493|NXNNNNNXNNNNNXNNNNNXNNNNNXNNNNNXNNNNNNNNNNNNNNNNXXXX483-517|504-496|468-532|534-466|NNNNXXXX0-529|0-461|0-0|495-505|508-492|NNSNNNSS487-513|NX'


def get_map_(index):
    map_ = np.array([[ -1,  -1,  -1],
                     [ -1,  -1,  -1],
                     [ -1,  -1,  -1]])
    b = ''
    while index > 0:
        b = b+str(index % 3)
        index = index // 3
    b = b+(9-len(b))*'0'
    for i in range(3):
        for j in range(3):
            map_[j, i] = int(b[j+i*3]) - 1

    return map_


def get_Xchances_Ochances(map_):
    X_chances = np.array([[-1.0, -1.0, -1.0],
                          [-1.0, -1.0, -1.0],
                          [-1.0, -1.0, -1.0]])
    O_chances = np.array([[-1.0, -1.0, -1.0],
                          [-1.0, -1.0, -1.0],
                          [-1.0, -1.0, -1.0]])
    for i in range(3):
        for j in range(3):
            ID = get_index(map_[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3])
            Pw = gg[ID][0]
            Pl = gg[ID][1]

            X_chances[i, j] = float(Pw)
            O_chances[i, j] = float(Pl)
    return X_chances, O_chances


def get_common_chances(common_map, X_chances, O_chances):
    current_winner = winner(common_map)
    if current_winner == 1:
        return 1, 0, 0
    if current_winner == 0:
        return 0, 1, 0
    free_cells = np.argwhere(common_map == -1)
    if free_cells.size == 0:
        return 0, 0, 1

    outcomes = np.array([0, 0, 0])
    for t in range(1000):
        np.random.shuffle(free_cells)
        current_winner = -1
        step = -1
        for step in range(free_cells.shape[0]):
            i, j = free_cells[step]
            dice = round(random.uniform(0, 100000))
            a, b = X_chances[i, j] * 100000, (X_chances[i, j] + O_chances[i, j]) * 100000
            if dice < a:
                common_map[i, j] = 1
            elif dice < b:
                common_map[i, j] = 0
            else:
                common_map[i, j] = 2
            current_winner = winner(common_map)
            if current_winner != -1:
                break
        if current_winner == -1:
            current_winner = 2
        outcomes[current_winner] += 1
        for k in range(step + 1):
            common_map[free_cells[k][0], free_cells[k][1]] = -1
    outcomes = outcomes / 1000
    g = open("history", "r")
    t = g.read()
    g.close()
    t += ','.join(list(map(str, common_map.ravel()))+list(map(str, X_chances.ravel()))+list(map(str, O_chances.ravel())))
    t += ','+str(outcomes[1])+','+str(outcomes[0])+','+str(outcomes[2])
    g = open("history", "w")
    g.write(t+'\n')
    g.close()
    return outcomes[1], outcomes[0], outcomes[2]


def winner(map_):
    for i in range(0, 3):
        if map_[i, 0] == map_[i, 1] == map_[i, 2] != -1 != 2:
            return map_[i, 0]
        if map_[0, i] == map_[1, i] == map_[2, i] != -1 != 2:
            return map_[0, i]
    if map_[0, 0] == map_[1, 1] == map_[2, 2] != -1 != 2:
        return map_[0, 0]
    if map_[2, 0] == map_[1, 1] == map_[0, 2] != -1 != 2:
        return map_[i, 0]
    return -1


def is_leaf(map_):
    if winner(map_) != -1:
        return True
    for i in range(3):
        for j in range(3):
            if map_[i, j] == -1:
                return False
    return True


def get_index(map_):
    k = 0
    num = 0
    for i in range(3):
        for j in range(3):
            num += (map_[i, j]+1)*(3**k)
            k += 1
    return num


g = []
for i in t.split('|'):
    if i[0] in '0123456789':
        g.append(tuple(i.split('-')))
    else:
        for j in range(len(i)):
            if i[j] == 'X':
                g.append(('1000', '0'))
            elif i[j] == 'N':
                g.append(('0', '1000'))
            elif i[j] == 'S':
                g.append(('0', '0'))
            else:
                g.append(tuple(i[j:].split('-')))
                break
current = 0
gg = [(-1, -1)]*19683
for ind in range(19683):
    if gg[ind][0] == -1:
        MAP_ = get_map_(ind)
        MAP_D = copy.deepcopy(get_map_(ind))
        for i in range(3):
            for j in range(3):
                if MAP_[i, j] == 0:
                    MAP_D[i, j] = 1
                if MAP_[i, j] == 1:
                    MAP_D[i, j] = 0
        for i in range(4):
            gg[get_index(MAP_)] = float(g[current][0])/1000, float(g[current][1])/1000
            MAP_ = copy.deepcopy(np.rot90(MAP_))
            gg[get_index(MAP_D)] = float(g[current][1])/1000, float(g[current][0])/1000
            MAP_D = copy.deepcopy(np.rot90(MAP_D))
        MAP_ = copy.deepcopy(np.flip(MAP_, 0))
        MAP_D = copy.deepcopy(np.flip(MAP_D, 0))
        for i in range(4):
            gg[get_index(MAP_)] = float(g[current][0])/1000, float(g[current][1])/1000
            MAP_ = copy.deepcopy(np.rot90(MAP_))
            gg[get_index(MAP_D)] = float(g[current][1])/1000, float(g[current][0])/1000
            MAP_D = copy.deepcopy(np.rot90(MAP_D))
        current += 1





class Game:
    def __init__(self):
        self.chances = gg
        self.Xw = None
        self.Ow = None
        self.N = None
        self.map_ = np.array([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                              [-1, -1, -1, -1, -1, -1, -1, -1, -1]])

        self.common_map = np.array([[-1, -1, -1],
                                    [-1, -1, -1],
                                    [-1, -1, -1]])

    def step(self, opponent_row, opponent_col, list_of_action):
        if opponent_col != -1 and opponent_row != -1:
            self.map_[opponent_row, opponent_col] = 0
        best_row, best_col = self.score(1, 2, list_of_action)[1]
        self.map_[best_row, best_col] = 1
        return best_row, best_col

    def get_index(self, map_):
        return get_index(map_)

    def update_chances(self, common_map, map_):
        Xchances, Ochances = get_Xchances_Ochances(map_)
        self.Xw, self.Ow, self.N = get_common_chances(common_map, Xchances, Ochances)

    def score(self, player, n, list_of_action):
        if is_leaf(self.common_map) or n == 0:
            X_chances, O_chances = get_Xchances_Ochances(self.map_)
            Xw, Ow, N = get_common_chances(self.common_map, X_chances, O_chances)
            return Xw-Ow, None
        else:
            best_step, best_score = None, None
            for row_col in (list_of_action):
                i, j = row_col[0], row_col[1]

                self.map_[i, j] = player
                for a in range(3):
                    for b in range(3):
                        min_map = self.map_[3 * a:3 * (a + 1), 3 * b:3 * (b + 1)]
                        if is_leaf(min_map):
                            self.common_map[a, b] = winner(min_map)
                new_score = self.score(int(player == 0), n-1, self.get_list_of_action(i, j))[0]
                if best_score is None or new_score > best_score and player == 1:
                    best_step, best_score = (i, j), new_score
                if best_score is None or new_score < best_score and player != 1:
                    best_step, best_score = (i, j), new_score
                self.map_[i, j] = -1
                for a in range(3):
                    for b in range(3):
                        min_map = self.map_[3 * a:3 * (a + 1), 3 * b:3 * (b + 1)]
                        if not is_leaf(min_map):
                            self.common_map[a, b] = -1
            return best_score, best_step

    def get_list_of_action(self, y, x):
        list_of_actions = []
        x = 3*(x % 3)
        y = 3*(y % 3)
        if self.common_map[y//3, x//3] == -1:
            for i in range(y, y+3):
                for j in range(x, x+3):
                    if self.map_[i, j] == -1:
                        list_of_actions.append((i, j))
        else:
            for i in range(9):
                for j in range(9):
                    if self.map_[i, j] == -1 and self.common_map[i // 3, j // 3] == -1:
                        list_of_actions.append((i, j))
        return list_of_actions


if __name__ == '__main__':
    game = Game()
    while True:
        opponent_row, opponent_col = map(int, input().split())
        validActionCount = int(input())
        list_of_action = [([int(j) for j in input().split()])for i in range(validActionCount)]
        row, col = game.step(opponent_row, opponent_col, list_of_action)
        print(str(row)+' '+str(col))