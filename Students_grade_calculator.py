def calculate_grade(*scores, **adjustment):
  
    average_score = sum(scores) / len(scores)
    bouns = sum(adjustment.values())
    final_grade = average_score + bouns
    #final_grade = adjusted_score  
    return final_grade

final_grade = calculate_grade(85, 90, 78)
print(f"Final grade: {final_grade}")
final_grade = calculate_grade(70, 65, 80,attendance=5, project=10)
print(f"Final grade: {final_grade}")