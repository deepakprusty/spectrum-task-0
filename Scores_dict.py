import numpy as np
import matplotlib.pyplot as plt
scores = {"Day 1": 100, "Day 2": 108, "Day 3":112, "Day 4":115, "Day 5":150,
          "Day 6":178, "Day 7": 143, "Day 8": 132, "Day 9":190, "Day 10": 235,
          "Day 11":253, "Day 12": 298, "Day 13": 328, "Day 14":390, "Day 15": 257,
          "Day 16":288, "Day 17": 393, "Day 18": 425, "Day 19":458, "Day 20": 450,
          "Day 21":473, "Day 22": 333, "Day 23": 452, "Day 24":490, "Day 25": 495,
          "Day 26":488, "Day 27": 543, "Day 28": 532, "Day 29":590, "Day 30": 605}

scores = list(scores.values())

Days = 1+np.arange(30)

Mean = np.mean(scores)
Median = np.median(scores)
Min = min(scores)
Max = max(scores)

print("Mean of the Scores is: ",Mean)
print("Median of the Scores is: ",Median)
print("Minimum score is: ",Min)
print("Maximum score is: ",Max)

plt.plot(scores, Days)
plt.xlabel('Score')
plt.ylabel('Days')
plt.title('Score vs Days')
plt.show()
