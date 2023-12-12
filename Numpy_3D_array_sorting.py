import numpy as np

ab = np.array([[[1, 2, 3], [5, 9, 6], [7, 0, -3]],
               [[1, 2, 3], [5, 9, 6], [4, 0, -7]]])

# Flatten, sort, and reshape
sorted_reshaped_ab = np.sort(ab.flatten()).reshape(ab.shape)

print(sorted_reshaped_ab)
