#!/usr/bin/env bash
# From MCourtois

set -e

#xcode-select --install

sudo -H easy_install pip
sudo -H pip install --upgrade virtualenv

virtualenv .venv

. .venv/bin/activate
pip install --upgrade setuptools
pip install --upgrade ansible

ansible-playbook macbookpro.yml

deactivate
