# Program Name: assignment03-pie.py
# Description: Loads a CSV of people and creates a pie chart of their email domains
# Author: P-Sav


import pandas as pd  # handle CSV data
import matplotlib.pyplot as plt # create plots

# --- Load the CSV file ---
csv_path = r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\Assignments\Week-3\people-1000.csv"  # path to CSV
data = pd.read_csv(csv_path)  # read CSV into DataFrame
print(data.head()) # show first few rows


# --- Extract email domains ---
email_col = [c for c in data.columns if 'email' in c.lower()][0]    # detect email column
data['domain'] = data[email_col].apply(lambda x: str(x).split('@')[-1])  # extract text after '@'
print(data[['domain']].head())    


# --- Count domains ---
domain_counts = data['domain'].value_counts() # count how many of each domain
print(domain_counts.head(10))  


# --- Plot Pie Chart ---
plt.figure(figsize=(6, 6)) # set chart size
plt.pie(
    domain_counts,
    labels=list(domain_counts.index), # domain names
    autopct='%1.1f%%', # percentage format
    startangle=140, # rotate pie for style
    labeldistance=1.1, # push labels outward
    pctdistance=0.5, # move % inward
    textprops={'fontsize': 12, 'fontweight': 'normal', 'color': 'black'}  # % text colour and style
)

# --- Style title and layout ---
plt.title("Email Domain Distribution", fontsize=18, fontweight='bold')  # bold title
plt.tight_layout() # adjust spacing
plt.show() # display chart

