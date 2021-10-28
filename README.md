# PDGTest
Code for generating synthetic high-frequency (1Hz but could be increased if desired) Permanent Downhole Gauge (PDG) and/or pressure response data &amp; analyzing the created dataset with several different regression methods. Used for an undergraduate research project.

TabularGenerator.ipynb can be used to create a flow rate data of an arbitrary length for any kind of use. The notebooks named "data_generator.ipynb" uses the tabular data and superposition principle to create the pressure response data for an Infinite acting Radial Flow (IARF) type reservoir. Boundary effects were not necessary for the study but could be implemented in the future.

Folders "Onerate" and "Bigdata" has tabular flow rates that allows data generator notebooks to create 10000-point and 1 million-point datasets, respectively. The generated datasets are then subjected to a 5-psi pseudo-random Gaussian noise and outlier points that constitutes %1 of the dataset, with both positive and negative magnitudes of 50,75 and 100 psi.

Updates Planned:

•Writing both the tabular data generator and pressure response data generator (superposition function) in pure C to create a fast executable file that could be solely used as a "Pressure Response Data Generator".
•Wrapping a simple GUI around the Python code, which also includes advanced noise and/or outlier addition settings.

