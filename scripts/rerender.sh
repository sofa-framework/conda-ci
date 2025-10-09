#!/bin/bash

#requires:
# - conda-smithy
# - git

export RATTLER_BUILD_EXPERIMENTAL=true

CONDA_BUILD_CONFIG_FILE=$1
FEEDSTOCK_DIR=$2

# run conda smithy:
# conda smithy rerender --feedstock_config conda/configs/conda-build.yaml --feedstock_directory <recipe_folder>
conda smithy rerender --feedstock_config $CONDA_BUILD_CONFIG_FILE --feedstock_directory $FEEDSTOCK_DIR

# filter <recipe_folder>/.ci_support/*.yaml files from unused conda-forge specific fields, i.e.: 
# docker_image, channel_targets...
python scripts/filter_configs.py $FEEDSTOCK_DIR/.ci_support/*.yaml scripts/filter.yaml
