# Fourier-Analysis
This project can be used to get the Fourier series of any curve in the complex plane.

Steps to use:-
1) Create a folder and save the curve to be transformed.
2) Use Scan.py to scan the points in the curve.
   Input: Path to the image file
   Output: data.csv containing the coordinates of the points extracted from the curve.
4) If the curve is thick, or there are some other elements presents with the curve, there might be redundant points in the the scan.
   Generally, the clean function from Extrapolation.py removes the redundant points. However, if it might sometimes overclean the curve.
   In such cases, the user might require to edit the data.csv file manually to precisely remove unwanted data.
5) The user may also join multiple than one curves by merging their data, ensuring the continuity of points.
   The final file used for transformation should be named data.csv
6) Use Transform.py to find the coefficients of the fourier series.
   Input: Folder Name
   Output: P = coefficients of the positive terms of the Fourier series.
           N = coefficients of the negative terms of the Fourier series.
7) Copy the arrays P and N from the output 
