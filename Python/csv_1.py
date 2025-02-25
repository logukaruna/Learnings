import csv

data = [
    ["Name", "Email"],
    ["John Doe", "john@example.com"],
    ["Jane Doe", "=HYPERLINK(\"http://localhost:8082/Vulnerable_App/Login.jsp\", \"Click here\")"]
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for row in data:
        # Prefix formulas with a single quote to treat them as text
        safe_row = [f"'{cell}" if str(cell).startswith(("=", "+", "-", "@")) else cell for cell in row]
        writer.writerow(safe_row)