{
    "name": "Product S3 Gallery",
    "version": "17.0.1.0.0",
    "price": 49.0,
    "currency": "USD",
    "summary": "Upload product images to Amazon S3 or store them as binary",
    "category": "Product",
    "author": "Waydata",
    "depends": ["product"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
        "views/res_config_settings_views.xml"
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3"
}