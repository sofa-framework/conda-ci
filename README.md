## About

CI generating conda packages for SOFA.
Packages are uploaded on the [Anaconda channel `sofa-framework`](https://anaconda.org/sofa-framework/repo).

Only SOFA release are generated for now (no nightly or development versions).

## Build status

**Current SOFA version for conda packages: 23.12.01**

[![linux-64](https://github.com/sofa-framework/conda-ci/actions/workflows/build_publish_linux-64.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/build_publish_linux-64.yml) [![osx-64](https://github.com/sofa-framework/conda-ci/actions/workflows/build_publish_osx-64.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/build_publish_osx-64.yml) [![win-64](https://github.com/sofa-framework/conda-ci/actions/workflows/build_publish_win-64.yml/badge.svg)](https://github.com/sofa-framework/conda-ci/actions/workflows/build_publish_win-64.yml)

## Available packages

SOFA core:
  - **libsofa-core**: SOFA core runtime libraries
  - **libsofa-core-devel**: SOFA core development files (runtime libraries + headers + cmake files)
  - **sofa-gl**: SOFA.GL rendering library (devel version)
  - **sofa-gui-qt**: Qt based GUI library for SOFA (devel version)
  - **sofa-app**: SOFA runtime binaries (sofaRun) + required resources. Use this package if you want a full install of SOFA core, as it will install as well all the previously mentioned packages for SOFA core. 

External SOFA plugins:
  - **sofa-python3**: for macOS users, please read special instructions [here](#special-instructions-for-macOS-users).
  - **sofa-stlib**
  - **sofa-modelorderreduction**
  - **sofa-beamadapter**
  - **sofa-softrobots**

## Installing SOFA from conda

### Setup conda

#### Install miniforge conda distribution

If you are new to conda or do not have a recent conda version, consider installing miniforge available [here](https://github.com/conda-forge/miniforge). Miniforge is a conda distribution maintened by the conda-forge community, which is the most active open-source conda community. Miniforge is also preconfigured to use the conda-forge channel by default. 

#### Create & activate conda environment

```
conda create -n sofa-env
conda activate sofa-env
```

### Quick install (recommanded): Full SOFA core install with SofaPython3 plugin

```
conda install sofa-app sofa-python3 --channel sofa-framework
```

If you need additional plugins that are listed as available, please see below to install them.

### Custom installation of SOFA from these conda packages

You can install each of the previously mentioned package using conda command-line by specifying the `sofa-framework` custom channel. For example, if you want to install **only SOFA runtime libraries**, i.e. the `libsofa-core` package, use:

```
conda install libsofa-core --channel sofa-framework
```

or use the alternative modern notation:

```
conda install sofa-framework::libsofa-core
```

It is possible to list all the versions of each SOFA package that are available for your platform using `conda search` command. For example, searching versions for the `libsofa-core` package:

```
conda search libsofa-core --channel sofa-framework
```

## Special instructions for macOS users

There is a bug with the python / libpython version provided by conda and current SofaPython3 (see this [issue](https://github.com/sofa-framework/SofaPython3/issues/393) or related [PR](https://github.com/sofa-framework/SofaPython3/pull/394)).

If you need to use the `runSofa` executable with `SofaPython3` plugin, use the provided `runSofa_with_python script` (installed in the `bin/` directory as well) instead the classical `runSofa`.
