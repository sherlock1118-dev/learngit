import pandas as pd
import numpy as np
import os
import sys


#hello1
if __name__ == '__main__':
    file_path = 'C:\\Users\wonib\Desktop\8.29\h1.txt'
    file = pd.read_csv(file_path, header=None, sep='\\s+', engine='python',error_bad_lines=False, skip_blank_lines=False).fillna(4).astype(int)
    all_data = np.array(file)
    wins = np.array_split(all_data, all_data.shape[0]/15)
    data_final = pd.DataFrame(columns=np.arange(0, 4))
    for win in wins:
        win = win[np.argsort(win[:, 0])]
        data_moment = pd.DataFrame(columns=np.arange(0, 4))
        for i in range(1,5):
            small_win = win[win[:,0]==i]
            small_win = small_win[np.argsort(small_win[:, 1])]
            data_moment = pd.concat([data_moment, pd.DataFrame(small_win)])
        len4 = data_moment[data_moment[0] == 4].shape[0]
        data_moment[data_moment[0] == 4] = pd.DataFrame(np.zeros((len4, 4)),dtype='int')
        data_final = pd.concat([data_final, data_moment])
    data_final.to_csv('C:\\Users\wonib\Desktop\8.29\h1_reindex2.txt', header=None, index=None)

# hello2
"""if __name__ == '__main__':
     file_path = 'C:\\Users\wonib\Desktop\8.29\hello2.txt'
     file = pd.read_csv(file_path, header=None, sep='\\s+', engine='python', error_bad_lines=False,
                       skip_blank_lines=False).fillna(0).astype(int)
     all_data = np.array(file)
     print(all_data.shape[0])
     wins = np.array_split(all_data[: int(all_data.shape[0]/ 15)*15,:], all_data.shape[0]/ 15)
     data_final = pd.DataFrame(columns=np.arange(0, 2))
     for win in wins:
        print(win.shape[0])
        data_final = pd.concat([data_final, pd.DataFrame(win),pd.DataFrame(np.zeros((1, 2)), dtype='int')])

    data_final.to_csv('C:\\Users\wonib\Desktop\8.29\hello2_reindex.txt', header=None, index=None)"""


