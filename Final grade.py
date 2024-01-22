quiz1 =float(input('Please enter your first quiz score :'))

quiz2 =float(input('Please enter your second quiz score :'))

midterm_exam =float(input('Please enter your midterm exam score :'))

final_exam =float(input('Please enter your final exam score :'))

q = (quiz1 + quiz2) *(25 / 100)

m = midterm_exam *(25 / 100)

f = final_exam *(50 / 100)

Total_scores = q + m + f

last_stage = Total_scores * 5

if last_stage >= 90 :
    print('Good score! Your score is equal to: A')
elif last_stage >= 80 and last_stage < 90 :
    print('You were great, just be careful! Your score is equal to: B')
elif last_stage >= 70 and last_stage < 80 :
    print('Be more careful, I hope you do well in the next exam! Your score is equal to: C')
elif last_stage >= 60 and last_stage < 70 :
    print('Study more! Your score is equal to: D')
elif last_stage < 60 :
    print('This score is not good for you at all, try harder! Your score is equal to: E')