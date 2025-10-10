#!/bin/bash

set -e

git diff --exit-code -s $FEEDSTOCK_DIR/.ci_support/*.yaml

echo "NEEDS_UPDATE=$?" >> $GITHUB_ENV
