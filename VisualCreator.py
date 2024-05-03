
import json

# Assuming 'data' contains your JSON data
with open('Avito.json', encoding='utf-8-sig') as json_file:
    Avito_data = json.load(json_file)
with open('Youla.json', encoding='utf-8-sig') as json_file:
    Youla_data = json.load(json_file)
#with open('Meshok.json', encoding='utf-8-sig') as json_file:
    #Meshok_data = json.load(json_file)
data = {
    "Avito": Avito_data,
    "Meshok": Avito_data,
#    "Meshok": Meshok_data,
    "Youla": Youla_data
}


html_start = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Market Listings</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .scroll-container {
            
            white-space: nowrap;
            padding: 20px;
        }
        .market {
            background-color: #fff;
            display: inline-block;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-right: 20px;
            min-width: 600px; /* Увеличена минимальная ширина */
            white-space: normal; /* Позволяет тексту переноситься */
        }
        .market h3 {
            background-color: #007bff;
            color: #fff;
            margin: 0;
            padding: 10px 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-right: 20px; /* Ensure there's space between tables */
        }
        th, td {
            text-align: left;
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f8f9fa;
        }
        tr:hover {
            background-color: #f2f2f2;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center; margin-top: 20px;">Market Listings Overview</h1>
    <div class="scroll-container">
"""

html_end = """
    </div>
    <script>
        function sortTable(n, tableId) {
            var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
            table = document.getElementById(tableId);
            switching = true;
            // Set the sorting direction to ascending:
            dir = "asc";
            /* Make a loop that will continue until
            no switching has been done: */
            while (switching) {
                // Start by saying: no switching is done:
                switching = false;
                rows = table.rows;
                /* Loop through all table rows (except the
                first, which contains table headers): */
                for (i = 1; i < (rows.length - 1); i++) {
                    // Start by saying there should be no switching:
                    shouldSwitch = false;
                    /* Get the two elements you want to compare,
                    one from current row and one from the next: */
                    x = rows[i].getElementsByTagName("TD")[n];
                    y = rows[i + 1].getElementsByTagName("TD")[n];
                    /* Check if the two rows should switch place,
                    based on the direction, asc or desc: */
                    if (dir == "asc") {
                        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                            // If so, mark as a switch and break the loop:
                            shouldSwitch = true;
                            break;
                        }
                    } else if (dir == "desc") {
                        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                            shouldSwitch = true;
                            break;
                        }
                    }
                }
                if (shouldSwitch) {
                    /* If a switch has been marked, make the switch
                    and mark that a switch has been done: */
                    rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                    switching = true;
                    // Each time a switch is done, increase this count by 1:
                    switchcount++;
                } else {
                    /* If no switching has been done AND the direction is "asc",
                    set the direction to "desc" and run the while loop again. */
                    if (switchcount == 0 && dir == "asc") {
                        dir = "desc";
                        switching = true;
                    }
                }
            }
        }
    </script>
</body>
</html>
"""


def generate_market_div(market_name, listings, market_id):
    html_content = f"<div class='market'><h3>{market_name}</h3>"
    html_content += f"""
    <table id="{market_id}">
        <tr>
            <th onclick="sortTable(0, '{market_id}')">Name</th>
            <th onclick="sortTable(1, '{market_id}')">City/Description</th>
            <th onclick="sortTable(2, '{market_id}')">Price</th>
            <th>URL</th>
        </tr>
    """
    for item in listings:
        name = item.get("name", "N/A")
        city_or_description = item.get("city", item.get("description", "N/A"))
        price = item.get("price", "N/A")
        url = item.get("url", "#")
        html_content += f"""
            <tr>
                <td>{name}</td>
                <td>{city_or_description}</td>
                <td>{price}</td>
                <td><a href="{url}" target="_blank">Link</a></td>
            </tr>
        """

    html_content += "</table></div>"
    return html_content


html_body = ""
market_id = 0
for market, listings in data.items():
    market_id += 1  # Increment to ensure a unique ID for each table
    html_body += generate_market_div(market, listings, f"market-table-{market_id}")

html_content = html_start + html_body + html_end

# Writing the HTML content to a file
with open("market_listings_sortable.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML file 'market_listings_sortable.html' has been created successfully.")
