# Minimal loader for Vangelis
import urllib
urllib.request.urlretrieve("https://raw.githubusercontent.com/imics-lab/load_data_time_series/main/HAR/e4_wristband_Nov2019/twristar_load_dataset.py", filename="twristar_load_dataset.py")
urllib.request.urlretrieve("https://raw.githubusercontent.com/imics-lab/load_data_time_series/main/HAR/e4_wristband_Nov2019/ue4w_load_dataset.py", filename="ue4w_load_dataset.py")
from twristar_load_dataset import twristar_load_dataset
t_names = ['Downstairs', 'Jogging', 'Sitting', 'Standing', 'Upstairs', 'Walking']
channels_list = ['accel_ttl','bvp','eda', 'p_temp'] # all channels to be used
x_train, y_train, x_valid, y_valid, x_test, y_test \
                                = twristar_load_dataset(
                                    incl_val_group = True,
                                    keep_channel_list = channels_list)
print("Labeled TWristAR Dataset ndarray shapes:")
print(" X      y")
print("train",x_train.shape, y_train.shape)  
print("valid",x_valid.shape, y_valid.shape)
print("test ",x_test.shape, y_test.shape)                          
from ue4w_load_dataset import ue4w_load_dataset
unlabeled_X, _, _, ch_list = ue4w_load_dataset()
print("Shape unlabeled_X",unlabeled_X.shape)