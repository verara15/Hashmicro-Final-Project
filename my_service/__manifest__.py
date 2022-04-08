{
    "name": "Service Mesin", 
    "author": "Cynthia & Vera", 
    "version": "1.0.0", 
    "category": "Sales", 
    'website': '', 
    'summary': 'Project akhir', 
    'description': """
            module tentang form pengisian service mesin
        """,
    "depends": [        
        "sale", # penting, ini menandakan bahwa kita menambah / mengurangi fitur module sale,
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/service.xml" 
    ],
    "license": '', 
    'installable': True 
}
