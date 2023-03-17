import os
from pathlib import Path
import json
'''
binary_task_id_mappings = json.loads(Path("../data/raw/binary.txt").read_text())
BINARY_TASK_IDS = [int(x) for x in binary_task_id_mappings.keys()]

#methods = ["mode", "knn", "forest", "dl", "gain", "vae"]

methods = ["knn"]


for i in BINARY_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} binary_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")

'''


os.system(f"python run-experiment.py 737 mode experiment_test --missing-fractions 0.5 --missing-types MAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")
#os.system(f"python run-experiment.py 737 mode experiment_test --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")
#os.system(f"python run-experiment.py 737 knn experiment_test --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")
#os.system(f"python run-experiment.py 737 forest experiment_test --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")



'''
# Multi Experiments


multi_task_id_mappings = json.loads(Path("../data/raw/multi.txt").read_text())
MULTI_TASK_IDS = [int(x) for x in multi_task_id_mappings.keys()]

#methods = ["mode", "knn", "forest", "dl", "gain", "vae"]

methods = ["dl"]


for i in MULTI_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} multi_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")

# Binary Expermients

binary_task_id_mappings = json.loads(Path("../data/raw/binary.txt").read_text())
BINARY_TASK_IDS = [int(x) for x in binary_task_id_mappings.keys()]

methods = ["mode", "forest", "gain", "vae"]

#methods = ["forest", "vae", "gain"]


for i in BINARY_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} corrupted_binary_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")

# Binary Expermients

binary_task_id_mappings = json.loads(Path("../data/raw/binary.txt").read_text())
BINARY_TASK_IDS = [int(x) for x in binary_task_id_mappings.keys()]

methods = ["knn"]

#methods = ["forest", "vae", "gain"]


for i in BINARY_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} corrupted_binary_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")


# Regression Experiments

regression_task_id_mappings = json.loads(Path("../data/raw/regression.txt").read_text())
REGRESSION_TASK_IDS = [int(x) for x in regression_task_id_mappings.keys()]

#methods = ["mode", "knn", "forest", "dl", "gain", "vae"]

methods = ["mode", "vae", "gain"]


for i in REGRESSION_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} corrupted_regression_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")



# Binary Experiments

binary_task_id_mappings = json.loads(Path("../data/raw/binary.txt").read_text())
BINARY_TASK_IDS = [int(x) for x in binary_task_id_mappings.keys()]

#methods = ["mode", "knn", "forest", "dl", "gain", "vae"]

methods = ["dl"]


for i in BINARY_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} binary_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")



binary_task_id_mappings = json.loads(Path("../data/raw/binary.txt").read_text())
BINARY_TASK_IDS = [int(x) for x in binary_task_id_mappings.keys()]

methods = ["dl"]

#methods = ["forest", "vae", "gain"]


for i in BINARY_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} corrupted_binary_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")



# Regression Experiments

regression_task_id_mappings = json.loads(Path("../data/raw/regression.txt").read_text())
REGRESSION_TASK_IDS = [int(x) for x in regression_task_id_mappings.keys()]

#methods = ["mode", "knn", "forest", "dl", "gain", "vae"]

methods = ["mode", "knn", "forest", "dl", "vae", "gain"]


for i in REGRESSION_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} regression_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")



##### Corrupted Tests #####


# Binary Expermients

binary_task_id_mappings = json.loads(Path("../data/raw/binary.txt").read_text())
BINARY_TASK_IDS = [int(x) for x in binary_task_id_mappings.keys()]

methods = ["mode", "knn", "forest", "dl", "gain", "vae"]

#methods = ["forest", "vae", "gain"]


for i in BINARY_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} corrupted_binary_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")



# Multi Experiments


multi_task_id_mappings = json.loads(Path("../data/raw/multi.txt").read_text())
MULTI_TASK_IDS = [int(x) for x in multi_task_id_mappings.keys()]

#methods = ["mode", "knn", "forest", "dl", "gain", "vae"]

methods = ["mode", "knn", "forest", "dl", "vae", "gain"]


for i in MULTI_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} corrupted_multi_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")


# Regression Experiments

regression_task_id_mappings = json.loads(Path("../data/raw/regression.txt").read_text())
REGRESSION_TASK_IDS = [int(x) for x in regression_task_id_mappings.keys()]

#methods = ["mode", "knn", "forest", "dl", "gain", "vae"]

methods = ["mode", "knn", "forest", "dl", "vae", "gain"]


for i in REGRESSION_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} corrupted_regression_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")





##### Fully Observed Tests #####

# Binary Expermients

binary_task_id_mappings = json.loads(Path("../data/raw/binary.txt").read_text())
BINARY_TASK_IDS = [int(x) for x in binary_task_id_mappings.keys()]

#methods = ["mode", "knn", "forest", "dl", "gain", "vae"]

methods = ["forest", "dl", "vae", "gain"]


for i in BINARY_TASK_IDS:
    for j in methods:
        os.system(f"python run-experiment.py {i} {j} binary_experiment --missing-fractions 0.01,0.1,0.3,0.5 --missing-types MCAR,MAR,MNAR --strategies single_single,single_all --num-repetitions 3 --base-path ../results")

'''