# Generator - Flask project

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

### INSTALLATION

To install this tool type the following:

```
cp -R ~/gen_flask_pro/bin/   /root/scripts/gen_flask_pro/ver.1.0/
cp -R ~/gen_flask_pro/conf/  /root/scripts/gen_flask_pro/ver.1.0/
cp -R ~/gen_flask_pro/log/   /root/scripts/gen_flask_pro/ver.1.0/
```

### DEPENDENCIES

This tool requires these other modules and libraries:


* ats_utilities https://vroncevic.github.io/ats_utilities

### Tool structure

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_flask_pro/dev/python-tool-docs/gen_flask_pro.png)

```
.
├── bin
│   ├── flask_pro
│   │   ├── divisional
│   │   │   ├── divisional_builder.py
│   │   │   └── __init__.py
│   │   ├── functional
│   │   │   ├── functional_builder.py
│   │   │   └── __init__.py
│   │   ├── gen_pro.py
│   │   ├── __init__.py
│   │   ├── modular
│   │   │   ├── __init__.py
│   │   │   └── modular_builder.py
│   │   ├── project
│   │   │   ├── __init__.py
│   │   │   └── project_info.py
│   │   ├── project_builder
│   │   │   ├── base_builder.py
│   │   │   └── __init__.py
│   │   ├── read_template.py
│   │   ├── structure_selector.py
│   │   └── write_template.py
│   ├── gen_flask_pro.py
│   └── gen_flask_pro_run.py
├── conf
│   ├── gen_flask_pro.cfg
│   ├── gen_flask_pro_util.cfg
│   └── template
│       ├── struct_core
│       │   ├── manage_commands
│       │   │   ├── create_database.template
│       │   │   ├── create_data.template
│       │   │   ├── create_superuser.template
│       │   │   ├── drop_database.template
│       │   │   ├── __init__.template
│       │   │   ├── run_coverage.template
│       │   │   └── run_test.template
│       │   └── manage.template
│       ├── struct_division
│       │   ├── base
│       │   │   ├── forms.template
│       │   │   ├── __init__.template
│       │   │   ├── static
│       │   │   ├── templates
│       │   │   └── views.template
│       │   ├── configuration
│       │   │   ├── base_config.template
│       │   │   ├── development_config.template
│       │   │   ├── __init__.template
│       │   │   ├── production_config.template
│       │   │   └── testing_config.template
│       │   ├── __init__.template
│       │   ├── models
│       │   │   ├── __init__.template
│       │   │   ├── model_base.template
│       │   │   └── model_user.template
│       │   ├── tests
│       │   │   ├── base.template
│       │   │   ├── helpers.template
│       │   │   ├── __init__.template
│       │   │   ├── test__config.template
│       │   │   ├── test_main.template
│       │   │   └── test_user.template
│       │   └── user
│       │       ├── forms.template
│       │       ├── __init__.template
│       │       ├── static
│       │       ├── templates
│       │       └── views.template
│       ├── struct_division.json
│       ├── struct_function
│       │   ├── configuration
│       │   │   ├── base_config.template
│       │   │   ├── development_config.template
│       │   │   ├── __init__.template
│       │   │   ├── production_config.template
│       │   │   └── testing_config.template
│       │   ├── __init__.template
│       │   ├── models
│       │   │   ├── __init__.template
│       │   │   ├── model_base.template
│       │   │   └── model_user.template
│       │   ├── static
│       │   │   ├── base.css
│       │   │   ├── base.js
│       │   │   └── favicon.ico
│       │   ├── templates
│       │   │   ├── base
│       │   │   ├── _base.html
│       │   │   ├── errors
│       │   │   ├── footer.html
│       │   │   ├── header.html
│       │   │   └── user
│       │   ├── tests
│       │   │   ├── base.template
│       │   │   ├── helpers.template
│       │   │   ├── __init__.template
│       │   │   ├── test__config.template
│       │   │   ├── test_main.template
│       │   │   └── test_user.template
│       │   └── views
│       │       ├── base.template
│       │       ├── __init__.template
│       │       ├── user_login.template
│       │       ├── user_register.template
│       │       └── user.template
│       ├── struct_function.json
│       ├── struct_modul
│       │   ├── configuration
│       │   │   ├── base_config.template
│       │   │   ├── development_config.template
│       │   │   ├── __init__.template
│       │   │   ├── production_config.template
│       │   │   └── testing_config.template
│       │   ├── forms
│       │   │   ├── __init__.template
│       │   │   ├── user_login.template
│       │   │   └── user_register.template
│       │   ├── __init__.template
│       │   ├── models
│       │   │   ├── __init__.template
│       │   │   ├── model_base.template
│       │   │   └── model_user.template
│       │   ├── static
│       │   │   ├── favicon.ico
│       │   │   ├── main.css
│       │   │   └── main.js
│       │   ├── templates
│       │   │   ├── base
│       │   │   ├── _base.html
│       │   │   ├── errors
│       │   │   ├── footer.html
│       │   │   ├── header.html
│       │   │   └── user
│       │   ├── tests
│       │   │   ├── base.template
│       │   │   ├── helpers.template
│       │   │   ├── __init__.template
│       │   │   ├── test__config.template
│       │   │   ├── test_main.template
│       │   │   └── test_user.template
│       │   └── views
│       │       ├── base.template
│       │       ├── __init__.template
│       │       └── user.template
│       └── struct_module.json
└── log
    └── gen_flask_pro.log

```

### COPYRIGHT AND LICENCE

Copyright (C) 2018 by https://vroncevic.github.io/gen_flask_pro

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:
