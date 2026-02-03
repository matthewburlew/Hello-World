Product = input("What's the product name?").strip().lower()

match Product:
    case p if p.startswith("tech"):
        category="High Margin"
    case "electronics" | "gadgets":
        category="High Margin"
    case "clothing" | "apparel":
        category="Medium Margin"
    case "food" | "groceries":
        category="Low Margin"
    case _:
        category="Uncategorized - Review Needed"

print(f"Product: {Product} | Category: {category}")

                