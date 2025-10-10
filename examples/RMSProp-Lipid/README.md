1. Download files.
2. Run 
```
cgderiv @cgderiv_ref.args
```
This produces the 'model_ref.p' file necessary for  ```cgrem```. Bond and angle table files are provided from ```cgfm``` and held fixed during REM optimization. A model.txt file containing the pairwise spline coefficients obtained from ```cgfm``` are provided as a starting point for REM optimization.

3. Run
```
bash cgrem.sh
```
to execute ```cgrem```. This can be constructed in a for loop for iterative REM runs.