# import sqlite3
# import csv
# import os

# # Path to the History file
# history_file = os.path.expanduser('~/.var/app/com.brave.Browser/config/BraveSoftware/Brave-Browser/Default/History')

# # Connect to the database
# conn = sqlite3.connect(history_file)
# cursor = conn.cursor()

# # Execute the query with the new order
# cursor.execute("SELECT last_visit_time, visit_count, title, url FROM urls")

# # Write the results to a CSV file
# with open('brave_history.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(['Last Visit Time', 'Visit Count', 'Title', 'URL'])  # Header in new order
#     csv_writer.writerows(cursor)

# conn.close()

# print("Data exported to brave_history.csv")
import csv

# Open the input CSV file
with open('brave_history.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header

    # Open the output CSV file
    with open('processed_brave_history2.csv', 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)
        
        # Write the header to the output file
        csv_writer.writerow(['Last Visit Time', 'Visit Count', 'Title', 'URL', 'base_url', 'path'])  # Header in new order
        
        # Set to track URLs to remove duplicates
        seen_urls = set()
        
        # Process and write each row
        for i, row in enumerate(csv_reader):
            if i == 5:
                break
            url = row[3]
            if url in seen_urls:
                continue
            seen_urls.add(url)
            base_url = url.split('/')[2]
            path = '/'.join(url.split('/')[3:])
            row.append(base_url)
            row.append(path)
            csv_writer.writerow(row)
            print(row)