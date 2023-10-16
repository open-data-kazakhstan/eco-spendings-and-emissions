import json
from datapackage import Package

# Set the encoding to 'utf-8'
package = Package(encoding='utf-8')

# Specify the file paths with proper encoding
csv_files = [
    r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_am\data\unpiv.csv',
    r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_am\data\fin_eco_am.csv',
    r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_am\data\eco_rank.csv',
    r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_drop\data\eco_drop_rank.csv',
    r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_drop\data\eco_drop_regr.csv',
    r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_drop\data\unpiv_part2.csv',
    r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_comb\csv_comb.csv'
]

# Infer and load each CSV file
for csv_file in csv_files:
    package.infer(csv_file)

# Commit the data package
package.commit()

# Define the path to the output JSON file
output_json_path = r"C:\Users\USER\Desktop\Eco_project\datapackage.json"

# Serialize the data package's metadata to a JSON file with proper encoding
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(package.descriptor, json_file, ensure_ascii=False, indent=4)

print(f"Data package saved to {output_json_path}")