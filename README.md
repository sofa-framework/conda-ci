## About

CI generating conda packages and conda-based CI tools for SOFA.
Packages are uploaded on the [Anaconda channel `sofa-framework`](https://anaconda.org/sofa-framework/repo).

Only SOFA release are generated for now (no nightly or development versions).

## Conda package build status

![Dynamic YAML Badge](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsofa-framework%2Fconda-ci%2Frefs%2Fheads%2Fmaster%2Fconda%2Frecipes%2Fsofa%2Frecipe.yaml&query=%24.context.version&label=Sofa%20release&color=4dc71f) ![Dynamic YAML Badge](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsofa-framework%2Fconda-ci%2Frefs%2Fheads%2Fmaster%2F.github%2Fworkflows%2Fsofa-python3.yml&query=%24.jobs.build-publish-sofa-python3.strategy.matrix.python&label=Python%20versions) ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/libsofa?label=Supported%20platforms)
 
[![sofa](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa.yml) [![sofa-python3](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-python3.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-python3.yml) [![sofa-stlib](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-stlib.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-stlib.yml) [![sofa-modelorderreduction](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-modelorderreduction.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-modelorderreduction.yml) [![sofa-beamadapter](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-beamadapter.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-beamadapter.yml) [![sofa-softrobots](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-softrobots.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-softrobots.yml) [![sofa-cosserat](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-cosserat.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/sofa-cosserat.yml)

## Available conda packages

**SOFA core**

| Name | Version | Platforms | Description |
| :---------: | ----------- | ------- | ------ |
| ![Static Badge](https://img.shields.io/badge/libsofa-98c610) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/libsofa) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/libsofa) |  SOFA core runtime libraries |
| ![Static Badge](https://img.shields.io/badge/sofa--devel-98c610) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-devel) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-devel) |  SOFA core development files (runtime libraries + headers + cmake files) |
| ![Static Badge](https://img.shields.io/badge/sofa--gl-98c610) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-gl) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-gl) |  SOFA.GL rendering library (devel version) |
| ![Static Badge](https://img.shields.io/badge/sofa--gui--qt-98c610) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-gui-qt) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-gui-qt) |  Qt based GUI library for SOFA (devel version) |
| ![Static Badge](https://img.shields.io/badge/sofa--app-98c610) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-app) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-app) | SOFA runtime binaries (sofaRun) + required resources. Includes all SOFA core packages. |

**External SOFA plugins**

| Name | Version | Platforms | Description |
| :---------: | ----------- | ------- | ------ |
| [![Static Badge](https://img.shields.io/badge/sofa--python3-98c610)](https://github.com/sofa-framework/SofaPython3) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-python3) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-python3) |  Python bindings and scenes support. For macOS users, **please read** special instructions [here](#special-instructions-for-macOS-users). |
| [![Static Badge](https://img.shields.io/badge/sofa--stlib-98c610)](https://github.com/SofaDefrost/STLIB) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-stlib) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-stlib) | SOFA Template Library |
| [![Static Badge](https://img.shields.io/badge/sofa--modelorderreduction-98c610)](https://github.com/SofaDefrost/ModelOrderReduction) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-modelorderreduction) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-modelorderreduction) | Plugin to Reduce Model |
| [![Static Badge](https://img.shields.io/badge/sofa--beamadapter-98c610)](https://github.com/sofa-framework/BeamAdapter) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-beamadapter) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-beamadapter) | Plugin implementing Kirchhoff rods to simulate any 1D flexible structure |
| [![Static Badge](https://img.shields.io/badge/sofa--softrobots-98c610)](https://github.com/SofaDefrost/SoftRobots) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-softrobots) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-softrobots) |  Plugin containing components & method for soft robotics |
| [![Static Badge](https://img.shields.io/badge/sofa--cosserat-98c610)](https://github.com/SofaDefrost/Cosserat) | ![Conda Version](https://img.shields.io/conda/vn/sofa-framework/sofa-cosserat) | ![Conda Platform](https://img.shields.io/conda/pn/sofa-framework/sofa-cosserat) |  Plugin to simulate linear structures using Cosserat theory |

## Installing SOFA from conda

### Quick install (recommanded): Full SOFA core install with SofaPython3 plugin

```
conda install sofa-app sofa-python3 --channel sofa-framework
```

If you need additional plugins that are listed as available, please see below to install them.

### Custom install

#### Setup conda (if necessary)

##### Install miniforge conda distribution

If you are new to conda or do not have a recent conda version, consider installing miniforge available [here](https://github.com/conda-forge/miniforge). Miniforge is a conda distribution maintened by the conda-forge community, which is the most active open-source conda community. Miniforge is also preconfigured to use the conda-forge channel by default. 

##### Create & activate conda environment

```
conda create -n sofa-env
conda activate sofa-env
```

#### Install SOFA packages

You can install each of the previously mentioned package using conda command-line by specifying the `sofa-framework` custom channel. For example, if you want to install **only SOFA runtime libraries**, i.e. the `libsofa` package, use:

```
conda install libsofa --channel sofa-framework
```

or use the alternative modern notation:

```
conda install sofa-framework::libsofa
```

It is possible to list all the versions of each SOFA package that are available for your platform using `conda search` command. For example, searching versions for the `libsofa` package:

```
conda search libsofa --channel sofa-framework
```

## Special instructions for macOS users

There is a bug with the python / libpython version provided by conda and current SofaPython3 (see this [issue](https://github.com/sofa-framework/SofaPython3/issues/393) or related [PR](https://github.com/sofa-framework/SofaPython3/pull/394)).

If you need to use the `runSofa` executable with `SofaPython3` plugin, use the provided `runSofa_with_python script` (installed in the `bin/` directory as well) instead the classical `runSofa`.
