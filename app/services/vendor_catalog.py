VENDORS = [
    {
        "name": "Budget Grocery Store",
        "category": "Groceries",
        "description": "Affordable everyday grocery options."
    },
    {
        "name": "Smart Fashion Hub",
        "category": "Fashion",
        "description": "Budget-friendly clothing and accessories."
    },
    {
        "name": "Home Essentials",
        "category": "Home",
        "description": "Useful household products at reasonable prices."
    },
    {
        "name": "Event Supplies",
        "category": "Party",
        "description": "Decorations and supplies for small events."
    },
    {
        "name": "Jewelry Corner",
        "category": "Jewelry",
        "description": "Affordable jewelry options for different occasions."
    }
]


def get_vendors(category: str | None = None):
    if not category:
        return VENDORS

    return [
        vendor
        for vendor in VENDORS
        if vendor["category"].lower() == category.lower()
    ]