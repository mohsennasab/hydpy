
.. _configuration:

Configuration Tools
===================


The `conf` subpackage provides some hard coded files that configure some
aspects of *HydPy*.

The binary |numpy| file `a_coefficients_explicit_lobatto_sequence.npy`
provides the Runge-Kutta coefficients required by models subclassed from
|ELSModel|.  ToDo: use a platfrom-independent file format.

The XML schema file `HydPyConfigBase.xsd` is automatically generated based on
its template file `HydPyConfigBase.xsdt`, and defines the required and possible
contents of XML configuration files to be executed with function
|run_simulation|.
