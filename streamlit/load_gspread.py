import gspread


gc = gspread.service_account()
# https://greeksharifa.github.io/references/2023/04/10/gspread-usage/

gc = gspread.service_account()
sh = gc.open_by_url(
    "https://docs.google.com/spreadsheets/d/1v5ghuHtPR5GnD8qV60_JUhDZFMgKVB3nvN1uI9Tia0U"
)

worksheet = sh.get_worksheet(0)

list_of_lists = worksheet.get_all_values()
for i, row in enumerate(list_of_lists):
    if i < 9 or row[8] == "":
        continue
    # print(row)
    score_row = row[8:14]
    date = row[8]
    loser = row[9]
    loser_score = row[10]
    money = row[11]
    winner = row[12]
    winner_score = row[13]

    print(
        f"날짜: {date}, 패자팀: {loser}, 패자팀 점수: {loser_score}점, 패자팀 벌금: {money}원, 승자팀: {winner}, 승자팀 점수: {winner_score}점"
    )

    # ['2024.05.13', '한경만, 허동혁', '4', '₩1,000', '김상현, 김지훈', '11']
    # print(score_row)
    # for col in row:
    #     print(f"__ {col}")


# print(sh.sheet1.get('B10'))
# sh = gc.open("시즌5") # 스프레드시트 제목으로 설정할 것
#
# print(sh.sheet1.get('A1'))

# 결과: [['gspread test']]
