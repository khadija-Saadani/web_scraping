import requests
import json
import csv

# Parameters for the API request
count = 60
anchor = 0
country = 'GB'
country_language = 'en-GB'
query = 'jordan'

# URL of the Nike API endpoint
url = f'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=241B0FAA1AC3D3CB734EA4B24C8C910D&country={country}&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace({country})%26filter%3Dlanguage({country_language})%26filter%3DemployeePrice(true)%26searchTerms%3D{query}%26anchor%3D{anchor}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D{count}&language={country_language}&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D'

# Make GET request to the Nike API
response = requests.get(url=url)
output = json.loads(response.text)

# File name for output
csv_filename = 'nike_products.csv'


# Open CSV file in write mode
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create CSV writer object
    csvwriter = csv.writer(csvfile)
    
    # Write header row in CSV
    csvwriter.writerow(['Title', 'Subtitle', 'Price', 'Num', 'Color'])
    
    # Loop through each product and write to CSV
    for item in output['data']['products']['products']:
        title = item['title']
        subtitle = item['subtitle']
        
        # Extract price, num, and color if available
        if 'price' in item:
            price = item['price']
        else:
            price = ''
        
        if 'num' in item:
            num = item['num']
        else:
            num = ''
        
        if 'color' in item:
            color = item['color']
        else:
            color = ''
        
        # Write row to CSV file
        csvwriter.writerow([title, subtitle, price, num, color])

print(f"\nData written to '{csv_filename}' successfully.")
