django-datatables-scaffolding/
├── manage.py
├── requirements.txt
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── datatables/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── urls.py
│       ├── views.py
│       └── templatetags/
│           └── __init__.py
└── templates/
    ├── base.html
    ├── includes/
    │   ├── footer.html
    │   ├── head-css.html
    │   ├── head-js.html
    │   ├── navigation.html
    │   └── scripts.html
    └── datatables/
        ├── index.html
        └── table_ajax.html