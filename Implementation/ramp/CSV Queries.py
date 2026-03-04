"""
Given a CSV file, Find which finicity_institution is not deleted and also dedupe them.
input = 
id,finicity_institution_id,tag,is_deleted,created_at
1234,3,capital 1,false,2020-02-28T06:10:29.714Z
1235,2,bank 5 maybe,true,2019-02-28T06:10:29.714Z
1333,2,bank five,false,2020-03-28T06:10:29.714Z
1458,1,wells fargo business???,true,2020-06-30T05:10:29.714Z
1567,1,wells fargo business,false,2020-06-21T06:10:29.714Z
1889,2,bank 5,false,2020-04-30T06:10:29.714Z
1890,1,wells fargo CEO,false,2020-06-30T06:10:29.714Z
1891,3,capital one,false,2020-06-30T06:10:29.714Z

Find which finicity_institution is not deleted and also dedupe them.

Followup: Achieve the same result with a SQL query.
"""


from datetime import datetime
from sortedcontainers import SortedList
import csv

# first one that is created 
# based on f_id 
# tag should correspond to the institution that is being kept 
# can be any user input format -> strptime 

# using a dictionary or a hash to determine unique values and then store the create date in the dictionary to know what to compare to 

class FinicityApp:
    def __init__(self, csv_url: str):
        self.csv_url = csv_url
        self.institutions = {}
    
    def process_csv(self):
        with open(self.csv_url, 'r') as f:
            file_dict = csv.DictReader(f)
            
            for item in file_dict: # iterator
                if item['is_deleted'] == "True":
                    continue 

                if item['finicity_institution_id'] not in self.institutions or datetime.fromisoformat(self.institutions[item['finicity_institution_id']]['created_at']) < datetime.fromisoformat(item['created_at']):
                    self.institutions[item['finicity_institution_id']] = item
    
    def return_results(self):
        for f_id, item in self.institutions.items():
            print(f"{item["tag"]} ({item['finicity_institution_id']}): Created at {item['created_at']}") 

    def overwrite_csv(self):
        with open(self.csv_url, 'w') as f:
            fieldnames = ['id', 'finicity_institution_id', 'tag', 'is_deleted', 'created_at']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(item for item in self.institutions.values())

        with open(self.csv_url, 'r') as f:
            file_dict = csv.DictReader(f)

            for item in file_dict:
                print(item)

def main():
    app = FinicityApp("converted_data.csv")
    app.process_csv()
    app.return_results()
    app.overwrite_csv()

if __name__ == "__main__":
    main()
    
