import pandas as pd
import os


def delete_unused_columns(filename):
    f = pd.read_csv(filename)
    columns_labels = ['randomBalloon', 'maxPumps', 'nPumps', 'size', 'earnings', 'popped', 'date', 'gender (m/f)',
                      'age', 'participant']
    new_f = f[columns_labels]
    os.remove(filename)
    new_f.to_csv(filename, index=False)
