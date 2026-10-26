import numpy as np
import pandas as pd

import kagglehub

# Download latest version
path = kagglehub.dataset_download("robiulhasan21/cervical-cancer-image-largest-dataset")

print("Path to dataset files:", path)

