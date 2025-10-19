## About

CI generating conda packages and conda-based CI tools for SOFA.

**Important notes**

Packages are now hosted on Prefix.dev: [`sofa-framework`](https://prefix.dev/channels/sofa-framework). The new channel to be used is:
`https://prefix.dev/sofa-framework`. Please do not use the old Anaconda channel `sofa-framework` (packages will be removed from Anaconda servers soon). 

## Build status for latest release

![Conda Version](https://img.shields.io/badge/SOFA%20release%20-%20v25.06-green)
![Python versions](https://img.shields.io/badge/Python%20versions%20-%203.10%2C3.11%2C3.12%2C3.13-blue) ![Conda Platforms](https://img.shields.io/badge/Supported%20platforms-linux--64%20%7C%20linux--aarch64%20%7C%20osx--64%20%7C%20osx--arm64%20%7C%20win--64-lightgrey)

## Available conda packages

**SOFA core**

| Name | Description |
| --------- | ------ |
| **libsofa** |  SOFA core runtime libraries |
| **sofa-devel** |  SOFA core development files (runtime libraries + headers + cmake files) |
| **sofa-gl** |  SOFA.GL rendering library (devel version) |
| **sofa-app** | SOFA runtime binaries (sofaRun) + required resources. Includes all SOFA core packages. |

**External SOFA plugins**

| Name | Description |
| --------- | ------ |
| **sofa-python3** |  Python bindings and scenes support. For macOS users, **please read** special instructions [here](#special-instructions-for-macOS-users). |
| **sofa-stlib** | SOFA Template Library |
| **sofa-modelorderreduction** | Plugin to Reduce Model |
| **sofa-beamadapter** | Plugin implementing Kirchhoff rods to simulate any 1D flexible structure |
| **sofa-softrobots** | Plugin containing components & method for soft robotics |
| **sofa-softrobotsinverse** |  Plugin containing inverse method for soft robotics |
| **sofa-cosserat** |  Plugin to simulate linear structures using Cosserat theory |
| **sofa-glfw** | Quick and simple GUI for SOFA, based on GLFW and optionally Dear ImGui |
| **sofa-qt** |  Qt based GUI library for SOFA (devel version) |

## Installing SOFA latest release from conda

### Important notes

Since last SOFA release 25.06, the default GUI has changed from Sofa.Qt to Sofa.ImGui.

### Quick install (recommanded)

#### Full SOFA core install with SofaPython3 plugin

```
conda install sofa-app sofa-python3 --channel https://prefix.dev/sofa-framework --channel conda-forge
```

Or
#### Full SOFA core install with all packaged plugins

```
conda install sofa-app sofa-python3 sofa-stlib sofa-modelorderreduction sofa-beamadapter sofa-softrobots sofa-cosserat --channel https://prefix.dev/sofa-framework --channel conda-forge
```
### Testing install

Run SOFA application with its GUI

```
runSofa -l SofaImGui -g imgui
```

Run SOFA application with its GUI **and** SofaPython3 plugin

```
runSofa -l SofaImGui -g imgui -l SofaPython3
```

Please open an [issue](https://github.com/sofa-framework/conda-ci/issues) to report any problem.

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
conda install libsofa --channel https://prefix.dev/sofa-framework
```

It is possible to list all the versions of each SOFA package that are available for your platform using `conda search` command. For example, searching versions for the `libsofa` package:

```
conda search libsofa --channel https://prefix.dev/sofa-framework
```

## Special instructions for macOS users

There is a bug with the python / libpython version provided by conda and current SofaPython3 (see this [issue](https://github.com/sofa-framework/SofaPython3/issues/393) or related [PR](https://github.com/sofa-framework/SofaPython3/pull/394)).

If you need to use the `runSofa` executable with `SofaPython3` plugin, use the provided `runSofa_with_python script` (installed in the `bin/` directory as well) instead the classical `runSofa`.

