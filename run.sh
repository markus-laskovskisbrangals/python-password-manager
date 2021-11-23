#!/bin/bash

echo "Python password manager setup script"
echo "-------------------------------------"

echo "Checking if required files exist"
if test -f "manager_log.yaml.dev"; then echo "File exists"; else echo "manager_log.yaml.dev not found"; exit 1; fi
if test -f "migration_log.yaml.dev"; then echo "File exists"; else echo "migration_log.yaml.dev not found"; exit 1; fi
if test -f "config.ini.template"; then echo "File exists"; else echo "config.ini.template not found"; exit 1; fi

echo "--------------------------------------"

echo "Renaming Files..."
mv manager_log.yaml.dev manager_log.yaml
if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying manager_log.yaml.dev file"; exit 1; fi
mv migration_log.yaml.dev migration_log.yaml
if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying migration_log.yaml.dev file"; exit 1; fi
mv config.ini.template config.ini
if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying config.ini.template file"; exit 1; fi

echo "Running setup.py"
python3 setup.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Problems with setup.py"; exit 1; fi
python3 test_config.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Problems with test_config.py"; exit 1; fi
python3 test.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Problems with setup.py"; exit 1; fi

echo "Setup successfull"
echo "To use password manager run command:"
echo "python3 generator.py"