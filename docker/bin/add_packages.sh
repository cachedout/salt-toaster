#!/bin/bash
set -e

# make sure the package repository is up to date
zypper --non-interactive --gpg-auto-import-keys ref

#zypper -n in --no-recommends python-devel python-pytest
zypper -n in --no-recommends python-devel python-pip
pip install pytest

