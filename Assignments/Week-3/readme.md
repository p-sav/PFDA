#### 1. assignment03-pie.py Program

When you run this notebook, it will load a CSV file containing people’s email addresses, extract their email **domains**, count how many times each occurs,  
and display the results as a **pie chart**


#### 2. What was learned :cd:
    - How to load CSV data using pandas
    - How to manipulate text columns in a DataFrame  
    - How to count unique values  
    - How to create and label a pie chart using matplotlib


#### 3. Program Code :floppy_disk:

```python
import pandas as pd  # handle CSV data
import matplotlib.pyplot as plt # create plots

# --- Load the CSV file ---
csv_path = r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\Assignments\Week-3\people-1000.csv"  # path to CSV
data = pd.read_csv(csv_path)  # read CSV into DataFrame
print(data.head())            # show first few rows


# --- Extract email domains ---
email_col = [c for c in data.columns if 'email' in c.lower()][0]    # detect email column
data['domain'] = data[email_col].apply(lambda x: str(x).split('@')[-1])  # extract text after '@'
print(data[['domain']].head())    


# --- Count domains ---
domain_counts = data['domain'].value_counts() # count how many of each domain
print(domain_counts.head(10))  


# --- Plot pie chart ---
plt.figure(figsize=(6, 6)) # set chart size
plt.pie(domain_counts, labels=domain_counts.index, autopct='%1.1f%%', startangle=140)  # create pie chart
plt.title("Email Domain Distribution") # add title
plt.show() # display chart
```

#### 4. Program Output :computer:

![Image showing the output of the program](/Assignments/Week-3/Figure_1.png)


#### 5. Summary

The project can can be found here: **github** <https://github.com/p-sav/PFDA/tree/main/Assignments/Week-3>


#### 6. References

1. OpenAI. (2025). *ChatGPT*, accessed October 2025, available at: https://chat.openai.com/
2. [Pandas](https://pandas.pydata.org/)
5. [Matplotlib](https://matplotlib.org/)
4. [Juypter Notebook](https://jupyter.org/)
5. [W3Schools](https://www.w3schools.com/python/)