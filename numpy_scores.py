# task 1 - Generate and Inspect the Data
import numpy as np
np.random.seed(42)
scores = np.random.randint(50, 101, size=(5, 4))
print("Scores:\n", scores)

score_3rd_2nd = scores[2, 1]
print("\n3rd student, 2nd subject:", score_3rd_2nd)

last_two = scores[-2:, :]
print("\nLast 2 students:\n", last_two)

subset = scores[:3, 1:3]
print("\nFirst 3 students, subjects 2 & 3:\n", subset)

# task 2 - Analyze with Broadcasting
col_means = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise means:", col_means)

curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve
curved_scores = np.clip(curved_scores, 0, 100)
print("\nCurved scores:\n", curved_scores)

row_max = curved_scores.max(axis=1)
print("\nRow-wise max values:", row_max)

# task 3 - Normalize and Identify
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)
normalized = (curved_scores - row_min) / (row_max - row_min)
print("\nNormalized scores:\n", normalized)

max_index = np.unravel_index(np.argmax(normalized), normalized.shape)
print("\nHighest normalized value at (student, subject):", max_index)

above_90 = curved_scores[curved_scores > 90]
print("\nCurved scores > 90:", above_90)