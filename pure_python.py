# 파일 연결자 f 만들기
f = open("scores.csv", "r", 
         encoding="utf-8")

# 파일 전체 읽기
lines = f.readlines()
f.close()

# 헤더, 카테고리 인덱스, 점수 인덱스 추출
header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

# 전체 인덱스 대상 반복 순회하며 데이터 읽기
# count = 0
count, totals, counts = 0, {}, {}
for lines in lines[1:]:
    parts = lines.strip().split(",")
    raw = parts[score_idx].strip()

    # 점수가 비어있으면, 다음 라인으로 패스 처리
    # 미제출 코드 스킵 처리
    # if raw == "" or raw == "미제출":
    #     # 이번 줄은 건너뛰고 다음 줄로 이동한다는 의미
    #     continue

    # try-except 구문으로 점수를 변환하고, 실패 시에는 ValueError 예외를 처리하여 다음 라인으로 이동
    try:
        score = float(raw)
    except ValueError:
        continue

    count += 1

    category = parts[cat_idx]
    # print(totals)
    
    # 카테고리가 totals 딕셔너리에 없으면 초기화 수행
    if category not in totals:
        totals[category] = 0.0
        counts[category] = 0

    # 누적합 구하기
    totals[category] += score
    counts[category] += 1

# 평균 계산 및 출력
for c in sorted(totals.keys()):
    # 키 기반으로 누적합 기반 평균 계산
    avg = totals[c] / counts[c]
    # round로 반올림하여 출력
    print(c, round(avg, 2))




