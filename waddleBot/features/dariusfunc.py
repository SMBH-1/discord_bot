import random
from sodapy import Socrata


#Randomly generates a MegaMillions number with conditions
def generate():
    pos1 = random.randrange(1, 70)
    pos2 = random.randrange(1, 70)
    pos3 = random.randrange(1, 70)
    pos4 = random.randrange(1, 70)
    pos5 = random.randrange(1, 70)
    megaball = random.randrange(1, 25)
    lotto_nums = set([pos1, pos2, pos3, pos4, pos5])
    while len(lotto_nums) < 5:
        lotto_nums = list(lotto_nums)
        lotto_nums.append(random.randrange(1, 70))
        lotto_nums = set(lotto_nums)
    lotto_nums = list(lotto_nums)
    lotto_nums.sort()
    lotto_nums.append(megaball)
    if does_not_exist(lotto_nums) & lotto_conditions(lotto_nums):
        str1 = ' '
        return str1.join([str(elem) for elem in lotto_nums])
    return generate()

# API call to recieve a full list of all mega millions winnning numbers
def get_all_lotto():
    client = Socrata("data.ny.gov", None)
    results = client.get("5xaw-6ayf", limit=3000)
    data = []
    exclude_nums = [71, 72, 73, 74, 75]
    for lotto_data in results:
        nums = lotto_data['winning_numbers']
        mega = lotto_data['mega_ball']
        format_nums = [int(nums[0]+nums[1]), int(nums[3]+nums[4]), int(nums[6]+nums[7]),
                       int(nums[9]+nums[10]), int(nums[12]+nums[13]), int(mega)]
        # Filter results with current rules for MegaMillions: 5 different numbers from 1 to 70 and 1 number from 1 to 25
        if set(format_nums).isdisjoint(set(exclude_nums)) and (format_nums[5] < 26):
            data.append(format_nums)
    return data

#API call to recieve latest drawing
def get_latest_draw():
    client = Socrata("data.ny.gov", None)
    results = client.get("5xaw-6ayf", limit=1)
    date =results[0]['draw_date'][0:10]
    latest_lotto = results[0]['winning_numbers'] + " "+results[0]['mega_ball']
    output = f"Lastest Draw Date: {date}\nWinning Numbers: {latest_lotto} "
    return output

def lotto_conditions(picks):
    all_sums = [] #List of sums from adding numbers winning numbers 1-5
    all_ranges = [] #List of the ranges from 1st number to 5th number
    all_adj_diff = [] #List of least and greatest adjacent differences ex: [2nd - 1st, 5th - 4th]
    possible_range = list(range(4,70))
    range_occur = dict(zip(possible_range, (0 for num in possible_range))) #Dictionary of range occurrences
    data = get_all_lotto()
    for lotto in data:
        sum = 0
        diff_1_2 = lotto[1] - lotto[0]
        diff_2_3 = lotto[2] - lotto[1]
        diff_3_4 = lotto[3] - lotto[2]
        diff_4_5 = lotto[4] - lotto[3]
        adj_diff = [diff_1_2,diff_2_3,diff_3_4,diff_4_5]
        adj_diff.sort()
        adj_diff = [adj_diff[0], adj_diff[3]]
        all_adj_diff.append(adj_diff)
        for num in lotto[0:5]:
            sum += num
        lotto_range = lotto[4] - lotto[0]
        all_sums.append(sum)
        all_ranges.append(lotto_range)
    for occur in all_ranges:
        range_occur[occur] += 1
    all_sums = list(set(all_sums))
    all_sums.sort() 
    all_ranges = list(set(all_ranges))
    all_ranges.sort()
    all_adj_diff = [list(pair) for pair in set(tuple(row) for row in all_adj_diff)]
    all_adj_diff.sort()
    #Condition Status
    passed_adj_diff = False
    passed_range = False
    passed_sum = False
    picks_sum = 0
    for num in picks[0:5]:
        picks_sum += num
    picks_diff_1_2 = picks[1] - picks[0]
    picks_diff_2_3 = picks[2] - picks[1]
    picks_diff_3_4 = picks[3] - picks[2]
    picks_diff_4_5 = picks[4] - picks[3]
    picks_adj_diff = [picks_diff_1_2,picks_diff_2_3,picks_diff_3_4,picks_diff_4_5]
    picks_adj_diff.sort()
    picks_adj_diff = [picks_adj_diff[0], picks_adj_diff[3]]
    picks_range = picks[4] - picks[0]
    #Checking if conditions are passed
    if picks_adj_diff in all_adj_diff:
        print('passed adjacent differences',picks_adj_diff)
        passed_adj_diff = True
    if picks_sum in all_sums:
        print('passed sum',picks_sum)
        passed_sum = True
    if picks_range in all_ranges:
        print('passed range',picks_range)
        passed_range = True
    return passed_adj_diff & passed_range & passed_sum

#Checking picks 1-5 against all winning numbers
def does_not_exist(picks):
    exists = []
    for lotto in get_all_lotto():
        if ((set(picks[0:5]) & set(lotto[0:6])) == set(picks)):
            exists.append(lotto)
    if len(exists) > 0:
        return False
    return True