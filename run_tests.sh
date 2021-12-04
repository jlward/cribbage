#! /bin/bash
rm -f .coverage*;  # Just in case, remove any existing coverage files.
coverage run ../venvs/cribbage/bin/nosetests $@ &&  # Run tests with coverage
coverage combine .coverage*; coverage report && # Combine coverage and report on them
echo 'Test are passing'
