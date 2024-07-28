# # # # open a csv file brave_history.csv and read the data from it. Then, print the first 5 rows of the data.
# # # # here's the data format
# # # # <epoch time>,<num>,<string>,<url>
# # # # example
# # # # Last Visit Time,Visit Count,Title,URL
# # # # 13365852078578692,1,25th word for Brave Sync time-limited words,https://alexeybarabash.github.io/25th-brave-sync-word/

# # # import csv
# # # #write each row to a new csv file called processed_brave_history.csv

# # # with open('brave_history.csv', 'r', newline='', encoding='utf-8') as csvfile:
# # #     csv_reader = csv.reader(csvfile)
# # #     next(csv_reader)  # Skip the header
# # #     for i, row in enumerate(csv_reader):
# # #         if i == 5:
# # #             break
# # #         url = row[3]
# # #         base_url = url.split('/')[2]
# # #         path = '/'.join(url.split('/')[3:])
# # #         row.append(base_url)
# # #         row.append(path)
# # #         sorted(row)
# # #         print(row)
# # # # Output:
# # # # ['13365852078578692', '1', '25th word for Brave Sync time-limited words', 'https://alexeybarabash.github.io/25th-brave-sync-word/']
# # import csv
# # from datetime import datetime

# # Open the input CSV file
# with open('brave_history.csv', 'r', newline='', encoding='utf-8') as csvfile:
#     csv_reader = csv.reader(csvfile)
#     next(csv_reader)  # Skip the header

#     # Open the output CSV file
#     with open('processed_brave_history.csv', 'w', newline='', encoding='utf-8') as outfile:
#         csv_writer = csv.writer(outfile)
        
#         # Write the header to the output file
        
#         header = next(csv_reader)
#         header.extend(['base_url', 'path'])
#         csv_writer.writerow(['Last Visit Time', 'Visit Count', 'Title', 'URL'])  # Header in new order
#         csv_writer.writerow(header)

#         # Process and write each row
#         for i, row in enumerate(csv_reader):
      
#             url = row[3]
#             base_url = url.split('/')[2]
#             path = '/'.join(url.split('/')[3:])
#             row.append(base_url)
#             row.append(path)
#             # Convert epoch time to YYYMMDD:HH:MM:SS format
#             epoch_time = int(row[0])
#             epoch_time = epoch_time // 1000000000
#             formatted_time = datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d_%H:%M:%S')
#             row.append(formatted_time)
#             csv_writer.writerow(row)
#             sorted(row)
#             if i <= 5:
#                 print(row)

# import csv

# # Open the input CSV file
# with open('brave_history.csv', 'r', newline='', encoding='utf-8') as csvfile:
#     csv_reader = csv.reader(csvfile)
#     next(csv_reader)  # Skip the header

#     # Open the output CSV file
#     with open('processed_brave_history2.csv', 'w', newline='', encoding='utf-8') as outfile:
#         csv_writer = csv.writer(outfile)
        
#         # Write the header to the output file
#         csv_writer.writerow(['Last Visit Time', 'Visit Count', 'Title', 'URL', 'base_url', 'path'])  # Header in new order
        
#         # Set to track URLs to remove duplicates
#         seen_urls = set()
        
#         # Process and write each row
#         for i, row in enumerate(csv_reader):
#             # if i == 5:
#             #     break
#             url = row[3]
#             if url in seen_urls:
#                 continue
#             seen_urls.add(url)
#             base_url = url.split('/')[2]
#             path = '/'.join(url.split('/')[3:])
#             row.append(base_url)
#             row.append(path)
#             csv_writer.writerow(row)
#             if i <= 5:
#                 print(row)

import csv
from datetime import datetime

# Open the input CSV file
with open('brave_history.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header

    # Open the output CSV file
    with open('processed_brave_history2.csv', 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)
        
        # Write the header to the output file
        header = next(csv_reader)
        header.extend(['base_url', 'path', 'formatted_time'])
        csv_writer.writerow(header)

        # Set to track URLs to remove duplicates
        seen_urls = set()
        
        # Process and write each row
        for i, row in enumerate(csv_reader):
            url = row[3]
            if url in seen_urls:
                continue
            seen_urls.add(url)
            base_url = url.split('/')[2]
            path = '/'.join(url.split('/')[3:])
            row.append(base_url)
            row.append(path)
            # Convert epoch time to YYYY-MM-DD_HH:MM:SS format
            epoch_time = int(row[0])
            epoch_time = epoch_time // 1000000  # Adjust the divisor if needed
            formatted_time = datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d_%H:%M:%S')
            row.append(formatted_time)
            csv_writer.writerow(row)
            if i <= 5:
                print(row)