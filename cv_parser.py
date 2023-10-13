import os
import pandas as pd
import spacy
spacy.load('en_core_web_sm')
from resume_parser import resumeparse

curr_path = os.getcwd()
path_for_cv_files = os.path.join(curr_path, "cv_samples")


all_files = os.listdir(path_for_cv_files)
file_locs =[]
for file_name in all_files:
    file_locs.append(os.path.join(path_for_cv_files, file_name))


# -----

cv_data = []
for cv in file_locs[:10]:
    cv_data.append(resumeparse.read_file(cv))

# -----

df = pd.DataFrame(cv_data)
# Fill NaN values with an empty string
df.fillna("", inplace=True)
df.replace([], '', inplace=True)


df.to_csv("partially_parsed_data.csv")