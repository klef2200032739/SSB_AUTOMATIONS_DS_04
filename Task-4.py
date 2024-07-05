import pandas as pd
import numpy as np

# Creating a sample dataset
np.random.seed(0)  # for reproducibility
n = 100  # number of samples

data = {
    'age': np.random.randint(18, 65, n),
    'income': np.random.normal(50000, 15000, n),
    'spending': np.random.normal(1000, 400, n)
}

df = pd.DataFrame(data)
# Calculate correlation matrix
correlation_matrix = df.corr()

print("Correlation Matrix:")
print(correlation_matrix)
