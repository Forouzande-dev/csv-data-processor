

# CSV Data Processor

import csv

def read_sales():
    with open("sales.csv" , encoding="utf-8") as file:
        
        rows = []
        reader = csv.DictReader(file)
        
        
        for row in reader:
            rows.append(row)
            
            row["quantity"] = int(row["quantity"])
            row["price"] = int(row["price"])
            row["total"] = row["quantity"] * row["price"]
            
            
    return rows



def save_report(total_sales, best_sales, total_quantity , average_sales):
    with open("sales.report.txt" , "w" , encoding="utf-8") as file:
        file.write("SALES REPORT \n")
        file.write(f"Total sales: {total_sales} \n")
        file.write(f"Best sales: {best_sales} \n")
        file.write(f"total quantity: {total_quantity} \n")
        file.write(f"Average sales: {average_sales} \n")
        
    
    
        
    
sales = read_sales()
print(sales)

total_sales = sum(row["total"] for row in sales)
print(f"Total Sales: {total_sales}")

best_sales = max(sales, key=lambda row:row["total"])
print(f"best sales: {best_sales}")

total_quantity = sum(row["quantity"] for row in sales)
print(f"total Quantity: {total_quantity}")

average_sales = total_sales / len(sales)
print(f"average sales: {average_sales}")

save_report(total_sales, best_sales, total_quantity , average_sales)