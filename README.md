# pyDGS-online

pyDGS-online - a web based framework for wavelet-based digital grain size analysis of [pyDGS](https://github.com/dbuscombe-usgs/pyDGS)

pyDGS is an open-source project dedicated to provide a Python framework to compute estimates of grain size distribution  using the continuous wavelet transform method of Buscombe (2013) from an image of sediment where grains are clearly resolved. DOES NOT REQUIRE CALIBRATION

This program implements the algorithm of:

Buscombe, D. (2013) Transferable Wavelet Method for Grain-Size Distribution from Images of Sediment Surfaces and Thin Sections, and Other Natural Granular Patterns. Sedimentology 60, 1709-1732

http://dbuscombe-usgs.github.io/docs/Buscombe2013_Sedimentology_sed12049.pdf

## Useage

### Install DGS by cloning the repository:
```bash
    $ python setup.py install
    $ sudo python setup.py install
    $ pip install pyDGS
```
    
### Test:
```bash
    $ python -c "import DGS; DGS.test.dotest()"
```

### Host on the web:
```bash
    $ export FLASK_APP=app.py
    $ flask run
```

## Contribution and Credits

_This is the web implementaion of the [pyDGS](https://github.com/dbuscombe-usgs/pyDGS)._
All the credits to the respective authors and developers.