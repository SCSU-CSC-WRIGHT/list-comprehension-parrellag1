def lab_1():
    num_scores = int(input("enter the number of score: "))
    scores_list = []
    for i in range(num_scores):
        score = float (input(f"enter score number {i+1}: "))
        scores_list.append(score)
        print(scores_list)
        avg_score = sum(scores_list)/len(scores_list)
        if avg_score >= 90:
            print("A", avg_score)
        elif avg_score >= 80 and avg_score < 90:
            print("B" avg_score)
        elif avg_score >= 70 and avg_score < 80:
            print("C" avg_score)
        elif avg_score >= 65 and avg_score < 70:
            print("D" avg_score)
        else:
            print("F", avg_score)
        lab_1()