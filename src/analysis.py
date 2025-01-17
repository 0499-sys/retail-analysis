import os
import matplotlib.pyplot as plt
from utils import connect_db, load_data, clean_data

# Paths
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
db_path = os.path.join(base_dir, "data/productsales.db")
report_path = os.path.join(base_dir, "report.md")

# Connect to the database and load data
conn = connect_db(db_path)
raw_data = load_data(conn)

# Clean the data
data = clean_data(raw_data)

sales_trends = data.groupby(['YEAR', 'ITEM TYPE'])['TOTAL_SALES'].sum().reset_index()

with open(report_path, "a") as f:
    f.write("\n## Sales Trends by Item Type\n")
    f.write(sales_trends.to_markdown(index=False))

visualizations = []
for year in sales_trends['YEAR'].unique():
    yearly_data = sales_trends[sales_trends['YEAR'] == year]
    plt.figure(figsize=(10, 6))
    plt.bar(yearly_data['ITEM TYPE'], yearly_data['TOTAL_SALES'])
    plt.title(f"Sales Trends in {year}")
    plt.xlabel("Item Type")
    plt.ylabel("Total Sales")
    
    # Save the visualization
    img_path = os.path.join(base_dir, f"data/productsales_{year}.png")
    plt.savefig(img_path)
    visualizations.append(img_path)
    plt.close()
    
with open(report_path, "a") as f:
    f.write("\n### Visualizations for Item Type Sales Trends\n")
    for img in visualizations:
        f.write(f"![Sales Trends in {os.path.basename(img).split('_')[-1].split('.')[0]}]({img})\n")

monthly_trends = data.groupby(['YEAR', 'MONTH'])['TOTAL_SALES'].sum().reset_index()

with open(report_path, "a") as f:
    f.write("\n## Monthly Sales Trends\n")
    f.write(monthly_trends.to_markdown(index=False))

for year in monthly_trends['YEAR'].unique():
    yearly_data = monthly_trends[monthly_trends['YEAR'] == year]
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_data['MONTH'], yearly_data['TOTAL_SALES'], marker='o')
    plt.title(f"Monthly Sales Trends in {year}")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(range(1, 13)) 
    plt.grid(True)
    
    img_path = os.path.join(base_dir, f"data/monthly_productsales_{year}.png")
    plt.savefig(img_path)
    visualizations.append(img_path)
    plt.close()

with open(report_path, "a") as f:
    f.write("\n### Visualizations for Monthly Sales Trends\n")
    for img in visualizations:
        if "monthly_trends" in img:
            f.write(f"![Monthly Trends in {os.path.basename(img).split('_')[-1].split('.')[0]}]({img})\n")

conn.close()