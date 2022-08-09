"""
This parser handles the reading and processing of flow controller or flow meter 
data. 

Usage
`````
Select :mod:`~yadg.parsers.flowdata` by supplying ``flowdata`` to the ``parser`` 
keyword, starting from :class:`DataSchema-4.0`. The following list of parameters is 
supported by the parser:

.. _yadg.parsers.flowdata.model:

.. autopydantic_model:: dgbowl_schemas.yadg.dataschema_4_2.step.FlowData.Params

.. _yadg.parsers.flowdata.formats:

Formats
```````
The formats currently supported by the parser are:

 - DryCal log file text output (``txt``): 
   :mod:`~yadg.parsers.flowdata.drycal`
 - DryCal log file tabulated output (``csv``): 
   :mod:`~yadg.parsers.flowdata.drycal`
 - DryCal log file document file (``rtf``): 
   :mod:`~yadg.parsers.flowdata.drycal`

.. _yadg.parsers.flowdata.provides:

Provides
````````
The parser is used to extract all tabular data in the input file. This parser processes 
additional calibration information analogously to :mod:`~yadg.parsers.basiccsv`. 
        
.. admonition:: DEPRECATED in ``yadg-4.2``

  The processing of calibration information has been deprecated in ``yadg-4.2``
  and will stop working in ``yadg-5.0``.

"""
from .main import process
