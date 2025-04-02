import joblib
from orcapy import ORCA
import argparse
from datetime import datetime

start_time = datetime.now() # you can remove this if you don't want to assess the time it takes to complete the job

parser = argparse.ArgumentParser(description="Find oriCs using ORCA.")
parser.add_argument("accession", help="The accession number to analyze")
args = parser.parse_args()

model = joblib.load("path/to/ORCA_RFC_model_1_4_0.pkl.gz") 
# this is the model provided by ORCA authors, and it can be downloaded directly from their github repository
email = "your_email"
accession_number = args.accession
orca = ORCA.from_accession(accession_number, email=email, model=model)
orca.find_oriCs(show_info=True, plot_path="/path/to/directory/to/store/plot")

# you can remove the code below this line if you don't want to assess the time it takes to complete the job
end_time = datetime.now()
execution_time = end_time - start_time

print(f"Execution time: {execution_time}")
