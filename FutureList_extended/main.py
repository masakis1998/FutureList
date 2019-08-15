from alist_fetch import get_alist
from merge_alist import merge_alist
from database_fetch import update_data
from anime_train_test_creation import create_train_test
from anime_score_prediction import predict_score
from result_combining import combine_results
from fscores_combining import combine_fscores
from result_labeling import lable_result
from train_graph import train_graph
from test_graph import test_graph
from column_name_adjust import process_column_name
from backup import create_backup
import os
import json
import sys

os.environ['KMP_DUPLICATE_LIB_OK']='True'

data = {"username": sys.argv[1], "rounds": sys.argv[2]}

with open("inputs.json", "w") as jsonFile:
    json.dump(data, jsonFile)

username = data['username']
rounds = data['rounds']

get_alist(username)
merge_alist()
update_data()
process_column_name()
create_train_test()
predict_score(int(rounds))
combine_results(int(rounds))
lable_result()
combine_fscores(int(rounds))
train_graph()
test_graph()
create_backup()

print('Finished all processes')

sys.exit()
