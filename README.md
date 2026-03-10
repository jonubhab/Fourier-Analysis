# Fourier-Analysis
This project can be used to get the Fourier series of any curve in the complex plane.

Files to be used:
01_Scan.py,
02_Transform.py,
03_Fourier Arts.json

Steps to use:-
1) Create a folder and save the curve to be transformed.
2) Use '01_Scan.py' to scan the points in the curve.
   1) Input: Path to the image file
   2) Output: data.csv containing the coordinates of the points extracted from the curve.
3) If the curve is thick, or there are some other elements presents with the curve, there might be redundant points in the the scan.
   Generally, the clean function from 'Extrapolation.py' removes the redundant points. However, if it might sometimes overclean the curve.
   See the plots to check for redundant points or overcleaning of data.
   In such cases, the user might require to edit the data.csv file manually to precisely remove unwanted data.
4) The user may also join multiple than one curves by merging their data, ensuring the continuity of points.
   The final file used for transformation should be named data.csv
5) Use Transform.py to find the coefficients of the fourier series.
   See the plots to check for curve fitting.
   1) Input: Folder Name
   2) Output:
      1) P = coefficients of the positive terms of the Fourier series.
      2) N = coefficients of the negative terms of the Fourier series.
6) Copy the contents of 'Fourier Arts.json' and paste it in Desmos Graphing Calculator.
   Or alternatively, open https://www.desmos.com/calculator/yvgav3i61q
7) Copy the arrays P and N from the output and paste them in Fourier Arts graph in Desmos, replacing the default arrays P and N.
8) Slide l to visualize the Fourier transform.

Example Usage:
Folder - Heart
1) Curve.png : The input curve
2) data.csv : Extracted points from curve
3) cfx.txt : Coefficients of fourier series along x-axis
4) cfy.txt : Coefficients of fourier series along y-axis
5) Heart.mp4 : Visualization
